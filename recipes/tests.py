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