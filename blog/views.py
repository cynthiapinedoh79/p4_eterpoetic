# /workspaces/p4_eterpoetic/blog/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return HttpResponse("Blog home OK")

def ping(request):
    return HttpResponse("pong")
