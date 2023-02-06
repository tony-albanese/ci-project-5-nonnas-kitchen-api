from django.test import TestCase
from .models import BlogPost
from kitchen_user.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='password')
    
    def test_user_can_list_posts(self):
        current_user = User.objects.get(username='test_user')
        BlogPost.objects.create(author=current_user, title='Test Title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post('/posts/', {'title': 'A test title.', 'body': 'test body'})
        count = BlogPost.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cant_post_if_not_logged_in(self):                
        response = self.client.post('/posts/', {'title': 'A test title.', 'body': 'test body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

