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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
