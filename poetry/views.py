from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Poem

def poem_list(request):
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")

    # Base queryset (newest first)
    qs = Poem.objects.all().order_by("-created")

    # Bilingual search
    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) |
            Q(title_en__icontains=q) |
            Q(body_es__icontains=q)  |
            Q(body_en__icontains=q)
        )

    total = qs.count()

    # Featured only when NOT searching and on the first page
    featured_poems = Poem.objects.none()
    if not q and (page_number in (None, "", "1")):
        featured_poems = qs.filter(is_featured=True).order_by("-created")[:3]
        # Exclude featured from the paginated list
        qs = qs.exclude(id__in=featured_poems.values("id"))

    # Paginate the remaining poems
    paginator = Paginator(qs, 9)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "poetry/poem_list.html",
        {
            "featured_poems": featured_poems,
            "page_obj": page_obj,
            "q": q,
            "total": total,
        },
    )

def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug=slug)
    return render(request, "poetry/poem_detail.html", {"poem": poem})
