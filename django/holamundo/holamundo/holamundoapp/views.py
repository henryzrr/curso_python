from django.shortcuts import render
from rest_framework import viewsets
from holamundo.holamundoapp.models import Computadora
from holamundo.holamundoapp.serializers import ComputadoraSerializer 
# Create your views here.
class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer