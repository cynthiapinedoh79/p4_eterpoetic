from django.urls import path
from . import views

app_name = "poetry"
urlpatterns = [
    path("", views.poem_list, name="poetryhome"),
    path("<slug:slug>/", views.poem_detail, name="detail"),
]

