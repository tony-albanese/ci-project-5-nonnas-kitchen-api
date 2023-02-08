from django.urls import path
from posts import views

urlpatterns = [
    path('recipes/'),
    path('recipes/<int:pk>/')
]