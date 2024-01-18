from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class ListTasks(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class CreateTasks(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class UpdateTasks(generics.RetrieveUpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class DeleteTasks(generics.DestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
