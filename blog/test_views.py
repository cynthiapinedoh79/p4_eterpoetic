from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        """Creates a blog post"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        """Verifies get request for post detail containing a comment form"""
        response = self.client.get(reverse(
        'blog:post_detail', args=['blog-title']), follow=True)   # ADD 'follow=True' to follow the 301 redirect to the 200 destination
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
    
    # def test_successful_comment_submission(self):
    #     """Test for posting a comment on a post"""
    #     self.client.login(
    #         username="myUsername", password="myPassword")
    #     post_data = {
    #         'body': 'This is a test comment.'
    #     }
    #     response = self.client.post(reverse(
    #         'post_detail', args=['blog-title']), post_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(
    #         b'Comment submitted and awaiting approval',
    #         response.content
    #     )
    
    # New (Using follow=True):
    
    
    # blog/test_views.py (Inside test_successful_comment_submission)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        # You must log in the user for a comment post
        self.client.login(username="myUsername", password="myPassword")
        
        # ADD/CORRECT THIS BLOCK:
        post_data = {
            'body': 'This is a test comment.',
        }
        
        response = self.client.post(reverse(
            'blog:post_detail', args=['blog-title']), 
            data=post_data, # This variable now exists
            follow=True) 
        # ... rest of the assertions