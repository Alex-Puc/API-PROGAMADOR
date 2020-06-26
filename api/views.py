from django.shortcuts import render

# Create your views here.

from .serializers import ProgrammerSerializer
from .models import Programmer
from rest_framework import generics


class ProgrammerList(generics.ListCreateAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class ProgrammerDetail(generics.RetrieveUpdateDestroyAPIView):
    query = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

