from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.


class BlogPostView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        context = {'request': request}
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True, context=context)

        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
