from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.BlogPostView.as_view()),
    path('posts/<int:id>', views.BlogPostDetailView.as_view()),
]