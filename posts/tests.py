from .models import BlogPost, Like
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

    def test_user_can_delete_their_own_post(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        BlogPost.objects.create(author=current_user, title='Test Title')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_post_not_their_own(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        BlogPost.objects.create(author=current_user, title='Test Title')
        self.client.logout()
        self.client.login(username='user_b', password='pass')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestLikeView(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

        blog_post_a = BlogPost.objects.get(id=1)
        blog_post_b = BlogPost.objects.get(id=2)

        Like.objects.create(owner=user_a, blog_post=blog_post_a)
        Like.objects.create(owner=user_a, blog_post=blog_post_b)
      
    def test_user_can_get_likes(self):
        response = self.client.get('/likes/')
        count = Like.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_post(self):
        current_user = User.objects.get(username='user_b')
        self.client.login(username='user_b', password='pass')
        blog_post_b = BlogPost.objects.get(id=2)
        response = self.client.post('/likes/', {'owner': current_user, 'blog_post':1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cant_like_post(self):
        current_user = User.objects.get(username='user_b')
        blog_post_b = BlogPost.objects.get(id=2)
        response = self.client.post('/likes/', {'owner': current_user, 'blog_post':1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_user_can_delete_own_like(self):
        current_user = User.objects.get(username='user_a')
        self.client.login(username='user_a', password='pass')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_likes(self):
        current_user = User.objects.get(username='user_b')
        self.client.login(username='user_b', password='pass')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_have_duplicate_likes(self):
        current_user = User.objects.get(username='user_a')
        self.client.login(username='user_a', password='pass')
        response = self.client.post('/likes/', {'owner': current_user, 'blog_post':1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)