from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from django.db import IntegrityError
from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    pass
