
from django.shortcuts import render
from rest_framework import generics
from appservidor.models import AutorDb,LibroDb
from .serializer import AutorDbSerializer,LibroDbSerializer
from rest_framework import viewsets

# Create your views here.
#Para el modelo Autor

class AutorDbAPIList(generics.ListAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer

class AutorDbAPICreate(generics.ListCreateAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer

class AutorDbAPIRetrieve(generics.RetrieveAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer

class AutorDbAPIDelete(generics.DestroyAPIView):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer

#Para el modelo Libros
class LibroDbAPIList(generics.ListAPIView):
    queryset = LibroDb.objects.all()
    serializer_class = LibroDbSerializer

class LibroDbAPICreate(generics.ListCreateAPIView):
    queryset = LibroDb.objects.all()
    serializer_class = LibroDbSerializer

class LibroDbAPIRetrieve(generics.RetrieveAPIView):
    queryset = LibroDb.objects.all()
    serializer_class = LibroDbSerializer

class LibroDbAPIDelete(generics.DestroyAPIView):
    queryset = LibroDb.objects.all()
    serializer_class = LibroDbSerializer

#viewsets
# En esta clase se ha definido operaciones de crear, listar, modificar, borrar
class AutorDbViewSet(viewsets.ModelViewSet):
    queryset = AutorDb.objects.all()
    serializer_class = AutorDbSerializer

