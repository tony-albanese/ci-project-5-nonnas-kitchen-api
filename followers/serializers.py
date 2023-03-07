from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    following_name = serializers.ReadOnlyField(source='following.username')
    follower_name = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'following_name', 'followed_on', 'follower', 'follower_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
