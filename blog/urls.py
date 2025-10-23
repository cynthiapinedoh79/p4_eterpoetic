# /workspaces/p4_eterpoetic/blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="list"),  # /en/ or /es/ will hit this
    path("ping/", views.ping, name="ping"),
    prefix_default_language=False,
]
