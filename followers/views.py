from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from .models import Follower

# Create your views here.


class FollowerListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(following=self.request.user)