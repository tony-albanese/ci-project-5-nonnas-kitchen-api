from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from django.db import IntegrityError
from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    '''
    What do I want to display to the user in a response?
    author 
    title 
    description
    dish_type 
    difficulty 
    time 
    time_unit 
    servings 
    ingredients_list 
    procedure
    tags 
    recipe_image 

    Cacluated fields:
    is_author
    number of likes
    likes_count
    number of comments
    '''
    pass
