from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from django.db import IntegrityError
from rest_framework import serializers
from .models import BlogPost, Like


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')
    is_liked = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()

    def validate_post_image(self, value):
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

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(blog_post=obj, owner=user).first()
            return like.id if like else None
        return None

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, blog_post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = BlogPost
        fields = [
            'id', 'author', 'title',  'body', 'category', 'posted_on',
            'post_image', 'is_author', 'profile_id', 'profile_image',
            'is_liked', 'like_id', 'likes_count', 'comments_count'
        ]


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_on', 'owner', 'blog_post'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate like'
            })
