from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost, Like
from .serializers import BlogPostSerializer, LikeSerializer
from kitchen.permissions import AuthorPermissions, OwnerPermissions
# Create your views here.


class BlogPostView(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorPermissions]
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [OwnerPermissions]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
