from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoApp
from .serializer import TodoSerializer


class TodoApiList(generics.ListAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer

class TodoApiCreateList(generics.CreateAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteUpdateGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoApp.objects.all()
    serializer_class = TodoSerializer


