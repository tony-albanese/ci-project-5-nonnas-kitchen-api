from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.BlogPostView.as_view()),
    path('posts/<int:id>/', views.BlogPostDetailView.as_view()),
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),

]