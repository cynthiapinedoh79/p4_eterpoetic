from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Poem

def _build_poem_list_context(request):
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    qs = Poem.objects.all().order_by("-created")
    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) | Q(title_en__icontains=q) |
            Q(body_es__icontains=q)  | Q(body_en__icontains=q)
        )
    total = qs.count()
    featured_poems = Poem.objects.none()
    if not q and (page_number in (None, "", "1")):
        featured_poems = qs.filter(is_featured=True).order_by("-created")[:3]
        qs = qs.exclude(id__in=featured_poems.values("id"))
    paginator = Paginator(qs, 9)
    page_obj = paginator.get_page(page_number)
    return {"featured_poems": featured_poems, "page_obj": page_obj, "q": q, "total": total}

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
        "hero_image_url": "/static/images/poetry-hero.jpg",
        "quotes": quotes,
        "hide_page_title": True,   # hide the big "Poems" H1 on the home page
    })
    return render(request, "poetry/home.html", ctx)
