from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.ProfileView.as_view()),
    path('profiles/<int:id>/', views.ProfileDetailView.as_view())
]
