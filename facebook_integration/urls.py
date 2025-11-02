from django.urls import path
from . import views

urlpatterns = [
    path("facebook/datadeletion/", views.fb_data_deletion, name="fb_data_deletion"),
    path("facebook/deauthorize/", views.fb_deauthorize, name="fb_deauthorize"),
]
