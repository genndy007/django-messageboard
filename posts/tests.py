from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
txt1 = 'just test'
txt2 = 'test 2'
posts_url = '/posts/'

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text=txt1)

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, txt1)

class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text=txt2)

    def test_view_url_exists_at_proper_location(self):
        res = self.client.get(posts_url)
        self.assertEqual(res.status_code, 200)

    def test_view_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
