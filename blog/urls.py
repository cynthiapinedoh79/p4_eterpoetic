from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/ - List view of all blog posts
    path('', views.PostList.as_view(), name='bloghome'),

    # /blog/<slug>/ - Detail view of a single blog post
    path('<slug:slug>/', views.post_detail, name='post_detail'),

    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

# Note: The 'app_name' variable is used to set the application
# namespace for URL reversing.
