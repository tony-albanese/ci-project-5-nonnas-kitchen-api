from django.db.models import Count
from rest_framework import permissions, generics, filters
from .models import Recipe, RecipeLike
from .serializers import RecipeSerializer, RecipeLikeSerializer
from kitchen.permissions import AuthorPermissions, OwnerPermissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class RecipeView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recipe.objects.annotate(
        likes_count=Count('recipe_likes', distinct=True)
    ).order_by('-posted_on')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    search_fields = [
        'author__username',
        'title',
    ]

    filterset_fields = [

        'author',
        'dish_type',
        'difficulty',
        'author__profile'  
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorPermissions]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    

class RecipeLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RecipeLikeSerializer
    queryset = RecipeLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeLikeDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [OwnerPermissions]
    serializer_class = RecipeLikeSerializer
    queryset = RecipeLike.objects.all()
