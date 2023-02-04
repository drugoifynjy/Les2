from django.shortcuts import render
from rest_framework import generics
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationAPIView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
