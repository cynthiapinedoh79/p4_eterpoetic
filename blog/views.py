# /workspaces/p4_eterpoetic/blog/views.py
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class PostList(generic.ListView):
    model = Post