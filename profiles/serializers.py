from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(following=user, follower=obj.owner).first()
            return following.id if following else None
        return None


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'first_name', 'last_name', 'created_on', 
            'bio', 'avatar', 'is_owner', 'following_id',
            'posts_count', 'follower_count', 'following_count'
        ]
