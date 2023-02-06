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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        
        self.assertEqual(response.data['title'], 'Test Title A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_with_invalid_id(self):
        response = self.client.get('/posts/1533434/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='user_a', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title', 'body': 'new body'})
        post = BlogPost.objects.filter(id=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='user_a', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title', 'body': 'new body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)