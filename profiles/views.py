from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from kitchen.permissions import OwnerPermissions
# Create your views here.


class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post_author', distinct=True),
        follower_count=Count('owner__follower', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__followed_on',
        'owner__follower__followed_on'

    ]


class ProfileDetailView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [OwnerPermissions]
 
    def get(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        self.check_object_permissions(self.request, profile)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
