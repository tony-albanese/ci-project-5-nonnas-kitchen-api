from django.shortcuts import render
from rest_framework import generics, permissions
from kitchen.permissions import AuthorPermissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
# Create your views here.

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [AuthorPermissions]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
