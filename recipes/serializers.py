from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from django.db import IntegrityError
from rest_framework import serializers
from .models import Recipe, RecipeLike


class RecipeSerializer(TaggitSerializer, serializers.ModelSerializer):
    '''
    What do I want to display to the user in a response?
    Cacluated fields:
    number of likes
    likes_count
    number of comments
    '''
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    dish_type_name = serializers.SerializerMethodField()
    posted_on = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')
    tags = TagListSerializerField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    
    def validate_recipe_image(self, value):
        if value.size > 1024*1024*2:
            raise serializers.ValidationError(
                'Image is larger than 2MB.'
            )
        if value.image.width > 2048 or value.image.height > 2048:
            raise serializers.ValidationError(
                'Image dimension error.'
            )
        return value

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_dish_type_name(self, obj):
        return obj.get_dish_type_display()

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = RecipeLike.objects.filter(
                owner=user, recipe=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'author', 'is_author', 'posted_on', 'title', 'description', 'dish_type',
            'dish_type_name', 'difficulty', 'time', 'time_unit', 'servings',
            'ingredients_list', 'procedure', 'tags', 'recipe_image', 
            'profile_id', 'profile_image', 'likes_count', 'like_id'
        ]


class RecipeLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = RecipeLike
        fields = [
            'id', 'owner', 'created_on', 'recipe'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate like'
            })