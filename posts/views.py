from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.


