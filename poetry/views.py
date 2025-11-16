from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from django.templatetags.static import static
from .models import Poem, Collection, Author  # <-- IMPORTANT: Import Author
from django.contrib.auth.decorators import login_required  # <-- NEW
from django.views.decorators.http import require_POST  # <-- NEW
from django.contrib import messages  # <-- NEW: Import messages framework

#
# DO NOT define models here
#


def _build_poem_list_context(request):
    """
    Builds the context for the poem/collection list pages.
    This is refactored to allow stacking filters.
    """
    q = (request.GET.get("q") or "").strip()
    page_number = request.GET.get("page")
    collection_slug = request.GET.get("collection")
    author_slug = request.GET.get("author")  # <-- NEW: Get author slug

    # Get all collections and authors for dropdowns
    all_collections = Collection.objects.all().order_by('name_en')
    all_authors = Author.objects.all().order_by('name')  # <-- NEW

    current_collection = None
    current_author = None  # <-- NEW: Track current author

    # --- NEW: Get logged-in user's favorite poem IDs ---
    favorite_poem_ids = []
    if request.user.is_authenticated:
        favorite_poem_ids = request.user.favorite_poems.values_list(
            'id', flat=True
        )
    # ----------------------------------------------------

    # --- Refactored Filter Logic ---

    # By default, we are in 'poems' mode and show all poems
    page_mode = 'poems'
    qs = Poem.objects.all().order_by('-is_featured', '-created')

    # 1. Apply search query if it exists
    if q:
        qs = qs.filter(
            Q(title_es__icontains=q) | Q(title_en__icontains=q) |
            Q(body_es__icontains=q) | Q(body_en__icontains=q) |
            Q(author__name__icontains=q)  # <-- BONUS: Also search author names
        )

    # 2. Apply collection filter if it exists
    if collection_slug and collection_slug != 'all-poems':
        try:
            current_collection = Collection.objects.get(slug=collection_slug)
            qs = qs.filter(collection=current_collection)
        except Collection.DoesNotExist:
            qs = Poem.objects.none()  # No poems

    # 3. Apply author filter if it exists
    if author_slug:
        try:
            current_author = Author.objects.get(slug=author_slug)
            qs = qs.filter(author=current_author)
        except Author.DoesNotExist:
            qs = Poem.objects.none()  # No poems

    # 4. Check if we should switch to 'collections' mode
    # This ONLY happens if no filters are applied at all.
    if not q and not collection_slug and not author_slug:
        page_mode = 'collections'
        qs = Collection.objects.all().order_by('name_en')

    # --- End of Refactored Logic ---

    # Now, paginate whatever qs is (either Collections or Poems)
    total = qs.count()
    paginator = Paginator(qs, 12)
    page_obj = paginator.get_page(page_number)

    return {
        "page_obj": page_obj,
        "page_mode": page_mode,
        "q": q,
        "total": total,
        "all_collections": all_collections,
        "all_authors": all_authors,  # <-- NEW: Pass authors to template
        "current_collection_slug": collection_slug,
        "current_collection": current_collection,
        "current_author_slug": author_slug,  # <-- NEW: Pass author slug
        "current_author": current_author,  # <-- NEW: Pass author object
        "favorite_poem_ids": favorite_poem_ids,  # <-- NEW: Pass IDs
    }


def poem_detail(request, slug):
    """Display a single poem's detail page.
    """
    poem = get_object_or_404(Poem, slug=slug)

    # --- NEW: Check if this single poem is a favorite ---
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = poem.favorites.filter(id=request.user.id).exists()
    # ----------------------------------------------------

    context = {
        "poem": poem,
        "is_favorite": is_favorite  # <-- NEW: Pass is_favorite
    }
    return render(request, "poetry/poem_detail.html", context)


def poem_list(request):
    """Display a list of poems or collections based on filters."""
    ctx = _build_poem_list_context(request)
    return render(request, "poetry/poem_list.html", ctx)


def poetry_home(request):
    """Display the poetry home page with hero image and quotes."""
    quotes = [
        {"text": "Feel the paper with the breathings of your heart",
         "author": "William Wordsworth"},
        {"text": "Creativity involves breaking out of established patterns...",
         "author": "Edward de Bono"},
        {"text": "Poetry is a spontaneous overflow of powerful feelings.",
         "author": "William Wordsworth"},
        {"text": "The chief enemy of creativity is good sense.",
         "author": "Pablo Picasso"},
        {"text": "Be yourself; everyone else is already taken.",
         "author": "Oscar Wilde"},
        {"text": "True poems are fires that burn and shine.",
         "author": "Vicente Huidobro"},
        {"text": "Poetry is the language of the soul.", "author": "Unknown"},
        {"text": "To try to express with words what the soul feels would "
                 "be like trying to trap the sea’s water in a container.",
         "author": "Marta Martín Girón"},
    ]
    ctx = _build_poem_list_context(request)
    ctx.update({
        "hero_image_url": static("images/poetry_hero.png"),
        "cover_image_url": static("images/poetry_cover.png"),
        "quotes": quotes,
        "hide_page_title": True,  # hide H1 on the home page
    })
    return render(request, "poetry/home.html", ctx)

# --- NEW: View for toggling a favorite ---


@login_required
@require_POST  # Ensures this view can only be accessed via POST
def toggle_favorite(request, poem_id):
    """Toggle a poem as a favorite for the logged-in user."""
    poem = get_object_or_404(Poem, id=poem_id)

    # Check if the poem is currently favorited
    is_favorited = poem.favorites.filter(id=request.user.id).exists()

    if is_favorited:
        # User has it as a favorite, so remove it
        poem.favorites.remove(request.user)
        # --- ADD FEEDBACK FOR REMOVAL ---
        messages.info(request, f"'{poem.title_en}' has been removed from your favorites.")
    else:
        # User does not have it as a favorite, so add it
        poem.favorites.add(request.user)
        # --- ADD FEEDBACK FOR ADDITION ---
        messages.success(request, f"'{poem.title_en}' has been added to your favorites! ❤️")

    # Redirect back to the page the user was on, which triggers the message display
    # (Assuming Poem model has a title_en field)
    return redirect(request.META.get('HTTP_REFERER', 'poetry:poetry_home'))


# --- NEW: View for the "My Favorites" page ---
@login_required
def favorites_list(request):
    """Display the logged-in user's favorite poems."""
    # Get all poems this user has favorited
    favorite_poems = request.user.favorite_poems.all().order_by(
        '-is_featured', '-created'
    )

    # We can reuse the main context builder but override the query
    ctx = _build_poem_list_context(request)

    # Paginate the favorite poems
    paginator = Paginator(favorite_poems, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Update context for this specific page
    ctx.update({
        "page_obj": page_obj,
        "page_mode": "poems",  # Always show poems
        "total": favorite_poems.count(),
        "is_favorites_page": True,  # A flag to change the page title
    })

    # We re-use the main poem_list template!
    return render(request, "poetry/poem_list.html", ctx)

def author_detail(request, slug):
    """
    Display an author's bio and a list of their poems.
    """
    author = get_object_or_404(Author, slug=slug)
    
    # Get all poems by this author
    # We order by featured first, then date, just like the main list
    poems = Poem.objects.filter(author=author).order_by('-is_featured', '-created')

    # --- Pagination ---
    paginator = Paginator(poems, 18)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # --- Favorites Logic (So hearts appear correctly) ---
    favorite_poem_ids = []
    if request.user.is_authenticated:
        favorite_poem_ids = request.user.favorite_poems.values_list('id', flat=True)

    context = {
        "author": author,
        "page_obj": page_obj,
        "favorite_poem_ids": favorite_poem_ids,
    }
    return render(request, "poetry/author_detail.html", context)
