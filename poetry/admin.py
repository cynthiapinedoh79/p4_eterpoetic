from django.contrib import admin
from .models import Author, Collection, Poem

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name_en", "slug")
    prepopulated_fields = {"slug": ("name_en",)}

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ("title_es", "author", "collection", "is_featured", "created")
    list_filter = ("collection", "is_featured")
    search_fields = ("title_es", "title_en", "body_es", "body_en")
    prepopulated_fields = {"slug": ("title_es",)}
    fields = (
        "author", "collection",
        "title_es", "body_es",
        "title_en", "body_en",
        "slug", "is_featured",
    )
