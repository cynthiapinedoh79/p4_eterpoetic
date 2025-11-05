from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.templatetags.static import static
from .models import Poem, Collection, Author  # <-- IMPORTANT: Import Author

#
# DO NOT define models here
#

def _build_poem_list_context(request):
    """
    Builds the context for the poem/collection list pages.
    This is refactored to allow stacking filters.
    """
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    collection_slug = request.GET.get("collection")
    author_slug = request.GET.get("author")  # <-- NEW: Get author slug

    # Get all collections and authors for dropdowns
    all_collections = Collection.objects.all().order_by('name_en')
    all_authors = Author.objects.all().order_by('name')  # <-- NEW: Get all authors

    current_collection = None
    current_author = None  # <-- NEW: Track current author
    
    # --- Refactored Filter Logic ---
    
    # By default, we are in 'poems' mode and show all poems
    page_mode = 'poems'
    qs = Poem.objects.all().order_by('-is_featured', '-created')

    # 1. Apply search query if it exists
    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) | Q(title_en__icontains=q) |
            Q(body_es__icontains=q)  | Q(body_en__icontains=q) |
            Q(author__name__icontains=q)  # <-- BONUS: Also search author names
        )

    # 2. Apply collection filter if it exists
    if collection_slug and collection_slug != 'all-poems':
        try:
            current_collection = Collection.objects.get(slug=collection_slug)
            qs = qs.filter(collection=current_collection)
        except Collection.DoesNotExist:
            qs = Poem.objects.none()  # No poems
    
    # 3. Apply author filter if it exists
    if author_slug:
        try:
            current_author = Author.objects.get(slug=author_slug)
            qs = qs.filter(author=current_author)
        except Author.DoesNotExist:
            qs = Poem.objects.none()  # No poems

    # 4. Check if we should switch to 'collections' mode
    # This ONLY happens if no filters are applied at all.
    if not q and not collection_slug and not author_slug:
        page_mode = 'collections'
        qs = Collection.objects.all().order_by('name_en')

    # --- End of Refactored Logic ---

    # Now, paginate whatever qs is (either Collections or Poems)
    total = qs.count()
    paginator = Paginator(qs, 12) 
    page_obj = paginator.get_page(page_number)
    
    return {
        "page_obj": page_obj, 
        "page_mode": page_mode,
        "q": q, 
        "total": total,
        "all_collections": all_collections,
        "all_authors": all_authors,  # <-- NEW: Pass authors to template
        "current_collection_slug": collection_slug,
        "current_collection": current_collection,
        "current_author_slug": author_slug,  # <-- NEW: Pass author slug
        "current_author": current_author,  # <-- NEW: Pass author object
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
