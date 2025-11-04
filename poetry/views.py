from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.templatetags.static import static
from .models import Poem, Collection  # <-- Correct: import from models.py

#
# DO NOT define models here
#

def _build_poem_list_context(request):
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    collection_slug = request.GET.get("collection")

    qs = Poem.objects.all()

    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) | Q(title_en__icontains=q) |
            Q(body_es__icontains=q)  | Q(body_en__icontains=q)
        )
    
    current_collection = None # <-- NEW: Initialize current_collection

    if collection_slug:
        # --- NEW: Get the actual Collection object ---
        try:
            current_collection = Collection.objects.get(slug=collection_slug)
            qs = qs.filter(collection=current_collection)
        except Collection.DoesNotExist:
            current_collection = None # Collection not found, no filtering
        # --- END NEW ---

    qs = qs.order_by('-is_featured', '-created')
    
    total = qs.count()
    
    paginator = Paginator(qs, 12) 
    page_obj = paginator.get_page(page_number)
    
    all_collections = Collection.objects.all().order_by('name_en')
    
    return {
        "page_obj": page_obj, 
        "q": q, 
        "total": total,
        "all_collections": all_collections,
        "current_collection_slug": collection_slug,
        "current_collection": current_collection, # <-- NEW: Pass the object
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
