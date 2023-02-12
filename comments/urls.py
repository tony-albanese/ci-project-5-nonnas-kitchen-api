from django.urls import path 
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('recipes/comments/', views.RecipeCommentList.as_view()),
    path('recipes/comments/<int:pk>/', views.RecipeCommentDetail.as_view())
]