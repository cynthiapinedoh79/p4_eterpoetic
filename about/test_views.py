from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content and initializes session"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

        # CRITICAL FIX: Force a session initiation for the test client
        session = self.client.session 
        session.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'), follow=True)

        # Assert status code
        self.assertEqual(response.status_code, 200)

        # REVERTED ASSERTION: Check for a unique, simple substring
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)


    # about/test_views.py (Inside test_successful_collaboration_request_submission)

# about/test_views.py (Inside test_successful_collaboration_request_submission)

    def test_successful_collaboration_request_submission(self):
        # ... your code starts here ...
        
        # INSERT THIS BLOCK
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        
        response = self.client.post(reverse('about'), data=post_data, follow=True)
        # ... rest of your code