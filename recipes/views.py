from django.db.models import Count
from rest_framework import permissions, generics, filters
from .models import Recipe
from .serializers import RecipeSerializer
from kitchen.permissions import AuthorPermissions, OwnerPermissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class RecipeView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recipe.objects.all()

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'author__username',
        'title',
        'dish_type',
        'difficulty'
    ]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorPermissions]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    