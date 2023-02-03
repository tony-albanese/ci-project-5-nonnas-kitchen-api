from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')
    tags = TagListSerializerField()

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
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'author', 'title',  'body','tags', 'posted_on', 'post_image', 'is_author','profile_id','profile_image',
        ]
