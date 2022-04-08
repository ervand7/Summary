from rest_framework import generics
from django.shortcuts import render
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
