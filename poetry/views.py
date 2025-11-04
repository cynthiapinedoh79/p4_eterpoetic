from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.templatetags.static import static
from .models import Poem

# This is the NEW, corrected function
#
# This is your NEW, simplified function for poetry/views.py
#
def _build_poem_list_context(request):
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    qs = Poem.objects.all() # Get all poems

    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) | Q(title_en__icontains=q) |
            Q(body_es__icontains=q)  | Q(body_en__icontains=q)
        )

    # --- START FIX ---
    # Order by featured status FIRST, then by date.
    # This puts all featured poems at the top of the list.
    qs = qs.order_by('-is_featured', '-created')
    # --- END FIX ---
    
    total = qs.count()

    # --- REMOVED THE OLD CONFUSING LOGIC ---
    
    # Paginate the *entire* list.
    # Your old page had 3 featured + 9 others, so let's set
    # the page size to 12.
    paginator = Paginator(qs, 12) 
    page_obj = paginator.get_page(page_number)
    
    return {
        # 'featured_poems' is no longer needed
        "page_obj": page_obj, 
        "q": q, 
        "total": total
    }

def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug=slug)
    return render(request, "poetry/poem_detail.html", {"poem": poem})

def poem_list(request):
    ctx = _build_poem_list_context(request)
    return render(request, "poetry/poem_list.html", ctx)

def poetry_home(request):
    quotes = [
        {"text": "Feel the paper with the breathings of your heart", "author": "William Wordsworth"},
        {"text": "Creativity involves breaking out of established patterns...", "author": "Edward de Bono"},
        {"text": "Poetry is a spontaneous overflow of powerful feelings.", "author": "William Wordsworth"},
        {"text": "The chief enemy of creativity is good sense.", "author": "Pablo Picasso"},
    ]
    ctx = _build_poem_list_context(request)
    ctx.update({
        "hero_image_url": static("images/poetry_hero.png"),
        "cover_image_url": static("images/poetry_cover.png"),
        "quotes": quotes,
        "hide_page_title": True,   # hide the big "Poems" H1 on the home page
    })
    return render(request, "poetry/home.html", ctx)
