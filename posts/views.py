from django.db.models import Count
from rest_framework import permissions, generics, filters
from .models import BlogPost, Like
from .serializers import BlogPostSerializer, LikeSerializer
from kitchen.permissions import AuthorPermissions, OwnerPermissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class BlogPostView(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = BlogPost.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-posted_on')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    filterset_fields = [
        'author__follower__following__profile',
        'likes__owner__profile',
        'author__profile'
    ]

    search_fields = [
        'author__username',
        'title'
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorPermissions]
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-posted_on')


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
