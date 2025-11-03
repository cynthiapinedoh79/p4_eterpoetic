# poetry/admin.py
from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
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
class PoemAdmin(SummernoteModelAdmin):
    # small preview in the list
    @admin.display(description="Image")
    def thumb(self, obj):
        if getattr(obj, "featured_image", None) and "placeholder" not in str(obj.featured_image):
            return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.featured_image.url)
        return "—"

    list_display = ("thumb", "title_es", "author", "collection", "is_featured", "created")
    list_filter = ("collection", "is_featured", "created")
    search_fields = ("title_es", "title_en", "body_es", "body_en")
    prepopulated_fields = {"slug": ("title_es",)}

    # show the upload widget on the form
    fields = (
        "author", "collection",
        "title_es", "body_es",
        "title_en", "body_en",
        "slug", "is_featured",
        "featured_image",          # ← important
    )

    # rich editor for poem bodies
    summernote_fields = ("body_es", "body_en")

@admin.display(description="Image")
def thumb(self, obj):
    if getattr(obj, "featured_image", None) and "placeholder" not in str(obj.featured_image):
        return format_html('<img src="{}" style="height:40px;border-radius:4px;">', obj.featured_image.url)
    return format_html('<img src="/static/images/placeholder.png" style="height:40px;border-radius:4px;opacity:0.6;">')


