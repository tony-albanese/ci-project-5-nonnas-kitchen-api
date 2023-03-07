from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework import status
from kitchen_user.models import User
from .models import Follower

# Create your tests here.


class TestFollowerListView(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')
        user_c = User.objects.create_user(username='user_c', password='pass')

        # Create a follower
        Follower.objects.create(following=user_a, follower=user_b)

    def test_get_all_followers(self):
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_follow_a_user(self):
        """
        In this test, user_a will follow user_c
        So user_a will login and follow user_c
        """
        self.client.login(username='user_a', password='pass')
        response = self.client.post('/followers/', {'following': 1, 'follower': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cant_follow_if_not_logged_in(self):
        """
        In this test, user_a will follow user_c without being logged in.
        """
        response = self.client.post('/followers/', {'following': 1, 'follower': 3})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_follow_user_twice(self):
        """
        In this test, user_a will try to follow user_b twice.
        So user_a will login and follow user_b. user_b has been followed in setUp()
        """
        self.client.login(username='user_a', password='pass')
        response = self.client.post('/followers/', {'following': 1, 'follower': 2})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestFollowerDetailView(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')
        user_c = User.objects.create_user(username='user_c', password='pass')

        # Create a follower
        Follower.objects.create(following=user_a, follower=user_b)

    def test_get_a_follower(self):
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unfollow_a_user(self):
        self.client.login(username='user_a', password='pass')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cant_unfollow_if_not_logged_in(self):
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
