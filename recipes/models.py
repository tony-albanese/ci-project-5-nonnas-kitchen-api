from django.db import models
from django.db.models import Avg
from kitchen_user.models import User
from base_models.models import AbstractLike, AbstractRating
from taggit.managers import TaggableManager
# Create your models here.


class Recipe(models.Model):
    DISH_TYPE = [
        ('app','Appetizer'),
        ('mains', 'Main Dish'),
        ('pasta', 'Pasta Dish'),
        ('meat', 'Meat Dish'),
        ('poultry', 'Poultry Dish'),
        ('vef', 'Vegetable Dish'),
        ('rice', 'Rice Dish'),
        ('pastry', 'Pastry'),
        ('dessert', 'Dessert')
    ]

    DIFFICULTY = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ]

    TIME_UNITS = [
        ('min', 'min'),
        ('hr', 'hours')
    ]

    TAGS = [
        'diabetic', 'gluten free', 'vegan', 'vegetarian', 'low calorie'
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    dish_type = models.CharField(max_length=7, choices=DISH_TYPE, default='app')
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY, default='easy')
    time = models.IntegerField(default=1)
    time_unit = models.CharField(max_length=3, default='hr', choices=TIME_UNITS)
    servings = models.IntegerField(default=1)
    ingredients_list = models.JSONField()
    procedure = models.JSONField()
    tags = TaggableManager(blank=True)
    recipe_image = models.ImageField(upload_to='images/', default='../blogpost_default_image_v2nwpm')
    posted_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_on']
        
    def __str__(self):
        return self.title

    def average_rating(self):
        return RecipeRating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"]


class RecipeLike(AbstractLike):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_likes')

    class Meta:
        unique_together = ['owner', 'recipe']
        ordering = ['created_on']

    def __str__(self):
        return f"Owner: {self.owner} Liked recipe: {self.recipe.title}"


class RecipeRating(AbstractRating):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ratings')

    class Meta:
        unique_together = ['owner', 'recipe']
        ordering = ['created_on']

    def __str__(self):
        return f"{self.recipe.title} Rating: {self.rating}"