"""
URL configuration for eterpoetic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns   # i18n
from blog import views   # <- import views if needed

urlpatterns = [
    # endpoint para cambiar idioma (lo usa el form del navbar)
    path("i18n/", include("django.conf.urls.i18n")),
]

# Rutas traducibles / prefijadas por idioma: /en/ ... /es/ ...
urlpatterns += i18n_patterns(
    path("", include("blog.urls"), name="blog-urls"),   # <- # ← blog, not posts
    path("admin/", admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    prefix_default_language=False,
)

# Solo si quieres servir media en desarrollo:
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
