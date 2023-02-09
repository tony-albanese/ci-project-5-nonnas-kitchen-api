from django.urls import path
from recipes import views

urlpatterns = [
    path('recipes/', views.RecipeView.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view())
]
