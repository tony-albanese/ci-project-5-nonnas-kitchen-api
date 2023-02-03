from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from kitchen.permissions import AuthorPermissions
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


class BlogPostDetailView(APIView):
    permission_classes = [AuthorPermissions]
    serializer_class = BlogPostSerializer

    def get(self, request, id):
        blog_post = get_object_or_404(BlogPost, id=id)
        serializer = BlogPostSerializer(
            blog_post, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, id):
        blog_post = get_object_or_404(BlogPost, id=id)
        serializer = BlogPostSerializer(
            blog_post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog_post = get_object_or_404(BlogPost, id=id)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)