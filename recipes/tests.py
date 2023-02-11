from .models import Recipe, RecipeLike
from kitchen_user.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class RecipeViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='password')
        current_user = User.objects.get(username='test_user')
        # create a recipe
        Recipe.objects.create(
            author=current_user,
            title='title',
            description='description',
            ingredients_list='{}',
            procedure='{}',
            tags=""
        )
          
    def test_user_can_get_list_of_recipes(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_recipe(self):
        recipe_data = {
            'title': 'test title 2',
            'description': 'a description',
            'ingredients_list': '{}',
            'procedure': '{}',
            'tags': "tag"
        }
        self.client.login(username='test_user', password='password')
        response = self.client.post('/recipes/', recipe_data)
        count = Recipe.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anonymous_user_cant_create_recipe(self):
        recipe_data = {
            'title': 'test title 2',
            'description': 'a description',
            'ingredients_list': '{}',
            'procedure': '{}',
            'tags': "tag"
        }
        response = self.client.post('/recipes/', recipe_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        Recipe.objects.create(
            author=user_a,
            title='title 1',
            description='description 1',
            ingredients_list='{}',
            procedure='{}',
            tags=""
        )

        Recipe.objects.create(
            author=user_a,
            title='title 2',
            description='description 2',
            ingredients_list='{}',
            procedure='{}',
            tags=""
        )

    def test_can_retrieve_recipe_with_valid_id(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['title'], 'title 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_recipe_with_invalid_id(self):
        response = self.client.get('/recipes/1533434/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='user_a', password='pass')

        updated_recipe_data = {
            'title': 'a new title',
            'description': 'a description',
            'ingredients_list': '{}',
            'procedure': '{}',
            'tags': "tag"
        }
        response = self.client.put('/recipes/1/', updated_recipe_data)
        post = Recipe.objects.filter(id=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipe(self):
        self.client.login(username='user_b', password='pass')

        updated_recipe_data = {
            'title': 'a new title',
            'description': 'a description',
            'ingredients_list': '{}',
            'procedure': '{}',
            'tags': "tag"
        }
        response = self.client.put('/recipes/1/', updated_recipe_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_recipe(self):
        self.client.login(username='user_a', password='pass')
        response = self.client.delete('/recipes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_recipe_not_their_own(self):
        self.client.login(username='user_b', password='pass')
        response = self.client.delete('/recipes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestRecipeLikes(APITestCase):

    def setUp(self):
        # Create two users.
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        # Create two Recipe objects.
        Recipe.objects.create(
            author=user_a,
            title='title 1',
            description='description 1',
            ingredients_list='{}',
            procedure='{}',
            tags=""
        )

        Recipe.objects.create(
            author=user_a,
            title='title 2',
            description='description 2',
            ingredients_list='{}',
            procedure='{}',
            tags=""
        )

        # Get references to the newly created recipes
        recipe_a = Recipe.objects.get(id=1)
        recipe_b = Recipe.objects.get(id=2)

        # Create two RecipeLikes. user_a will like both recipes.
        RecipeLike.objects.create(owner=user_a, recipe=recipe_a)
        RecipeLike.objects.create(owner=user_a, recipe=recipe_b)

    def test_user_can_get_recipe_likes(self):
        response = self.client.get('/recipes/likes/')
        count = RecipeLike.objects.count()
        self.assertEqual(count, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_like_a_recipe(self):
        current_user = User.objects.get(username='user_b')
        self.client.login(username='user_b', password='pass')
        response = self.client.post('/recipes/likes/', {'owner': current_user, 'recipe':1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cant_like_recipe(self):
        current_user = User.objects.get(username='user_b')
        response = self.client.post('/recipes/likes/', {'owner': current_user, 'blog_post':1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_recipe_like(self):
        current_user = User.objects.get(username='user_a')
        self.client.login(username='user_a', password='pass')
        response = self.client.delete('/recipes/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_recipe_likes(self):
        # current_user = User.objects.get(username='user_b')
        self.client.login(username='user_b', password='pass')
        response = self.client.delete('/recipes/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_have_duplicate_recipe_likes(self):
        current_user = User.objects.get(username='user_a')
        self.client.login(username='user_a', password='pass')
        response = self.client.post('/recipes/likes/', {'owner': current_user, 'blog_post':1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)