from . import views
from django.urls import path

urlpatterns = [
    # 1. Main /about/ page
    path('', views.about_me, name='about'),  # Matches: /about/

    # 2. List of all profiles (e.g., /about/all/)
    path('all/', views.profile_list, name='profile_list'),   # Matches: /about/all/
    
    # 3. Specific profile by its title (MUST BE LAST to avoid matching 'all/' or 'admin/')
    path('<str:profile_title>/', views.profile_detail, name='profile_detail'),
]