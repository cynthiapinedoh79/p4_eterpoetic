from django.urls import path
from . import views

app_name = "poetry"
urlpatterns = [
    path("", views.poem_list, name="poetryhome"),
    # IMPORTANT: prefix detail so it doesn't match /about/ or /blog/
    path("<slug:slug>/", views.poem_detail, name="poem_detail"),
]

