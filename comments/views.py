from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from kitchen.permissions import AuthorPermissions
from .models import Comment, RecipeComment
from .serializers import CommentSerializer, CommentDetailSerializer, RecipeCommentSerializer, RecipeCommentDetailSerializer
# Create your views here.


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'blog_post'
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [AuthorPermissions]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()


class RecipeCommentList(generics.ListCreateAPIView):
    serializer_class = RecipeCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RecipeComment.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'recipe'
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorPermissions]
    serializer_class = RecipeCommentDetailSerializer
    queryset = RecipeComment.objects.all()
