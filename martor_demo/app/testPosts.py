# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Mi Titulo", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "Mi Titulo")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")
