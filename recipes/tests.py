from .models import Recipe
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
        pass

    def test_cannot_retrieve_recipe_with_invalid_id(self):
        pass

    def test_user_can_update_own_recipe(self):
        pass

    def test_user_cant_update_another_users_recipe(self):
        pass

    def test_user_can_delete_their_own_recipe(self):
        pass

    def test_user_cannot_delete_recipe_not_their_own(self):
        pass