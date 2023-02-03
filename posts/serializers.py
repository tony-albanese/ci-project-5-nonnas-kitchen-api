from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = tags = TagListSerializerField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.avatar.url')
    tags = TagListSerializerField()
    
    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author
    

    class Meta:
        model = BlogPost
        fields = [
            'id', 'author', 'title',  'body','tags', 'posted_on', 'post_image', 'is_owner','profile_id','profile_image',
        ]
