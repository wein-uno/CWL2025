#from django.shortcuts import render
from rest_framework import viewsets
from .models import Comics
from .serializers import ComicsSerializer

class ComicsViewSet(viewsets.ModelViewSet):
       queryset = Comics.objects.all()
       serializer_class = ComicsSerializer


