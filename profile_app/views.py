from django.shortcuts import render
from rest_framework import viewsets, generics

# Create your views here.
from rest_framework.response import Response

from profile_app.models import Profile
from profile_app.serializers import ProfileSerializer, UserProfileSerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer