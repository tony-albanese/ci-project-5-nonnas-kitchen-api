from rest_framework import serializers
from .models import Comment, RecipeComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Comment
        fields = [
            'id', 'author', 'blog_post', 'body', 'created_on',
            'is_author', 'profile_id', 'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    blog_post = serializers.ReadOnlyField(source='blog_post.id')


class RecipeCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = RecipeComment

        fields = [
            'id', 'author', 'recipe', 'body', 'created_on', 'is_author', 'profile_id', 'profile_image',
        ]


class RecipeCommentDetailSerializer(RecipeCommentSerializer):
    recipe = serializers.ReadOnlyField(source='recipe.id')
