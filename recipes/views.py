from django.db.models import Count
from rest_framework import permissions, generics, filters
from .models import Recipe
from .serializers import RecipeSerializer
from kitchen.permissions import AuthorPermissions, OwnerPermissions
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class RecipeView(generics.ListCreateAPIView):
    pass
