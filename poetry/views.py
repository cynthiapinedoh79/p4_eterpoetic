from django.shortcuts import render, get_object_or_404
from .models import Poem

def poem_list(request):
    q = request.GET.get("q", "")
    poems = Poem.objects.all()
    if q:
        poems = poems.filter(title_en__icontains=q) | poems.filter(body_en__icontains=q)
    return render(request, "poetry/poem_list.html", {"poems": poems, "q": q})

def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug=slug)
    return render(request, "poetry/poem_detail.html", {"poem": poem})
