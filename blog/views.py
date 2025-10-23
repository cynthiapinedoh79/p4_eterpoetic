# /workspaces/p4_eterpoetic/blog/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog home OK")

def ping(request):
    return HttpResponse("pong")
