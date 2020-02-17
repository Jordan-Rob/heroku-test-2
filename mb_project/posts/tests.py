from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):
        post = Post.objects.create(text="just a test")
        self.post_id = post.pk

    def test_text_content(self):
        post = Post.objects.get(id=self.post_id)
        expected_obect_name = f'{post.text}'
        self.assertEqual(expected_obect_name, 'just a test')


class HomePageViewTest(TestCase):

    def test_url_location(self):
        post = Post.objects.create(text='this is just another test')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
