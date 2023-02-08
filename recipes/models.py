from django.db import models
from kitchen_user.models import User
from base_models.models import AbstractLike, AbstractRating
from taggit.managers import TaggableManager
# Create your models here.


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # type choice field
    # meal category choice field
    # difficulty choice field
    # time
    # time_unit
    # yield
    # ingredients list
    # procedure
    # tags : diabetic, gluten_free, vegan, vegetarian, low_calorie

    def __str__(self):
        return self.title


class RecipeLike(AbstractLike):
    pass


class RecipeRating(AbstractRating):
    pass

