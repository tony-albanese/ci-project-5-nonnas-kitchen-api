from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from kitchen.permissions import OwnerPermissions
# Create your views here.


class ProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [OwnerPermissions]
 
    def get(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        self.check_object_permissions(self.request, profile)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
