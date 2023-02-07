from .models import Comment, BlogPost
from kitchen_user.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class CommentViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='password')
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

    def test_view_all_comments(self):
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(id=1)
        comment = Comment.objects.create(author=current_user, blog_post=blog_post, body="Test body.")
        response = self.client.get('/comments/')
        count = Comment.objects.count()

        self.assertEqual(count,1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_can_create_comment_if_logged_in(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        response = self.client.post('/comments/', {'author': current_user, 'blog_post': 1, 'body': 'Test comment body'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_create_comment_if_anonymous(self):
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        response = self.client.post('/comments/', {'author': current_user, 'blog_post': 1, 'body': 'Test comment body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_update_their_own_comment(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        comment = Comment.objects.create(author=current_user, blog_post=blog_post, body="Test body.")
        response = self.client.put('/comments/1/', {'body': 'Updated comment body'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cannot_update_comment_if_not_owner(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        comment = Comment.objects.create(author=current_user, blog_post=blog_post, body="Test body.")
        self.client.logout()
        self.client.login(username='user_b', password='pass')
        response = self.client.put('/comments/1/', {'body': 'Updated comment body'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_comment(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        comment = Comment.objects.create(author=current_user, blog_post=blog_post, body="Test body.")
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_comment_if_not_owner(self):
        self.client.login(username='user_a', password='pass')
        current_user = User.objects.get(username='user_a')
        blog_post = BlogPost.objects.get(pk=1)
        comment = Comment.objects.create(author=current_user, blog_post=blog_post, body="Test body.")
        self.client.logout()
        self.client.login(username='user_b', password='pass')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

