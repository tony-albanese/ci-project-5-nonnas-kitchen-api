from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
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
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    filterset_fields = [
        'owner__following__follower__profile'
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__followed_on',
        'owner__follower__followed_on'

    ]


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [OwnerPermissions]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post_author', distinct=True),
        follower_count=Count('owner__follower', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_on')
 
