from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Collection, Poem

class PoetryViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        This is run once, so it's more efficient than setUp.
        """
        # Create an author
        cls.author = Author.objects.create(name="Test Author", slug="test-author")
        
        # Create two collections
        cls.col1 = Collection.objects.create(
            name_en="English Collection 1",
            slug="english-collection-1"
        )
        cls.col2 = Collection.objects.create(
            name_es="Colección Española 2",
            slug="coleccion-espanola-2"
        )
        
        # Create poems
        cls.poem1 = Poem.objects.create(
            title_en="Poem 1 (Featured)",
            slug="poem-1-featured",
            author=cls.author,
            collection=cls.col1,
            body_en="Body for poem 1.",
            is_featured=True
        )
        
        cls.poem2 = Poem.objects.create(
            title_es="Poema 2 (Bilingüe)",
            title_en="Poem 2 (Bilingual)",
            slug="poema-2-bilingue",
            author=cls.author,
            collection=cls.col1,
            body_en="English body.",
            body_es="Cuerpo en español."
        )
        
        cls.poem3 = Poem.objects.create(
            title_en="Poem 3 (Collection 2)",
            slug="poem-3-collection-2",
            author=cls.author,
            collection=cls.col2,
            body_en="Body for poem 3."
        )
        
        # Instantiate the client
        cls.client = Client()

    # --- Poem Detail View Tests ---

    def test_poem_detail_view_success(self):
        """Test that a valid poem slug returns 200 and the correct template/context."""
        url = reverse('poetry:poem_detail', args=[self.poem1.slug])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poetry/poem_detail.html')
        self.assertEqual(response.context['poem'], self.poem1)
        self.assertContains(response, "Poem 1 (Featured)")
        
        # Test that toggle buttons do NOT appear (only has English body)
        self.assertNotContains(response, 'id="btn-es"')

    def test_poem_detail_view_bilingual_toggle(self):
        """Test that toggle buttons appear for a bilingual poem."""
        url = reverse('poetry:poem_detail', args=[self.poem2.slug])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="btn-es"') # Check for ES button
        self.assertContains(response, 'id="btn-en"') # Check for EN button
        self.assertContains(response, "Cuerpo en español.") # Spanish body
        self.assertContains(response, "English body.") # English body
        
    def test_poem_detail_view_404(self):
        """Test that an invalid slug returns a 404."""
        url = reverse('poetry:poem_detail', args=['a-slug-that-does-not-exist'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # --- Home Page View Test ---

    def test_poetry_home_view_default(self):
        """Test the home page in its default state (showing collections)."""
        url = reverse('poetry:poetry_home')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poetry/home.html')
        
        # Test context specific to the `poetry_home` view
        self.assertTrue(response.context['hide_page_title'])
        self.assertIn('quotes', response.context)
        self.assertIn('hero_image_url', response.context)
        
        # Test context from _build_poem_list_context
        self.assertEqual(response.context['page_mode'], 'collections')
        self.assertEqual(response.context['total'], 2) # 2 collections
        self.assertIn(self.col1, response.context['page_obj'].object_list)
        self.assertIn(self.col2, response.context['page_obj'].object_list)
        
        # Check that poem titles are NOT rendered in collection mode
        self.assertNotContains(response, "Poem 1 (Featured)")

    # --- Poem List View Test (and Context Helper Logic) ---

    def test_poem_list_view_default(self):
        """Test the /poems/ list page in its default state (showing collections)."""
        url = reverse('poetry:poem_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poetry/poem_list.html')
        
        # Should NOT be hidden on the main list page
        self.assertFalse(response.context.get('hide_page_title', False)) 
        
        # Default mode is 'collections'
        self.assertEqual(response.context['page_mode'], 'collections')
        self.assertEqual(response.context['total'], 2) # 2 collections
        self.assertIn(self.col1, response.context['page_obj'].object_list)
        self.assertContains(response, "Collections") # The H1 title
        self.assertNotContains(response, "Poem 1 (Featured)")

    def test_list_view_all_poems(self):
        """Test the view with ?collection=all-poems."""
        url = reverse('poetry:poetry_home') + '?collection=all-poems'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['current_collection_slug'], 'all-poems')
        
        # Should contain all 3 poems
        self.assertEqual(response.context['total'], 3)
        self.assertIn(self.poem1, response.context['page_obj'].object_list)
        self.assertIn(self.poem2, response.context['page_obj'].object_list)
        self.assertIn(self.poem3, response.context['page_obj'].object_list)
        self.assertContains(response, "Poem 1 (Featured)")

    def test_list_view_specific_collection(self):
        """Test the view with ?collection=<slug>."""
        url = reverse('poetry:poetry_home') + f'?collection={self.col1.slug}'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['current_collection'], self.col1)
        
        # Should contain only the 2 poems from col1
        self.assertEqual(response.context['total'], 2)
        self.assertIn(self.poem1, response.context['page_obj'].object_list)
        self.assertIn(self.poem2, response.context['page_obj'].object_list)
        self.assertNotIn(self.poem3, response.context['page_obj'].object_list)
        
        # Should show the collection description card
        self.assertContains(response, "English Collection 1 Collection")

    def test_list_view_invalid_collection(self):
        """Test the view with ?collection=invalid-slug."""
        url = reverse('poetry:poetry_home') + '?collection=invalid-slug'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['current_collection'], None)
        self.assertEqual(response.context['total'], 0)
        self.assertContains(response, "No poems found.") # Empty state

    def test_list_view_search_title(self):
        """Test the view with ?q=... (searching titles)."""
        # Search for "Bilingüe" which is only in poem2's Spanish title
        url = reverse('poetry:poetry_home') + '?q=Bilingüe'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['q'], 'Bilingüe')
        
        # Should contain only poem2
        self.assertEqual(response.context['total'], 1)
        self.assertIn(self.poem2, response.context['page_obj'].object_list)
        self.assertNotIn(self.poem1, response.context['page_obj'].object_list)
        self.assertContains(response, "Poema 2 (Bilingüe)")

    def test_list_view_search_body(self):
        """Test the view with ?q=... (searching bodies)."""
        # Search for "Cuerpo" which is only in poem2's Spanish body
        url = reverse('poetry:poetry_home') + '?q=Cuerpo'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['total'], 1)
        self.assertIn(self.poem2, response.context['page_obj'].object_list)
        
    def test_list_view_search_no_results(self):
        """Test a search with no results."""
        url = reverse('poetry:poetry_home') + '?q=xyz_nonexistent_xyz'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_mode'], 'poems')
        self.assertEqual(response.context['total'], 0)
        self.assertContains(response, "No poems found.")