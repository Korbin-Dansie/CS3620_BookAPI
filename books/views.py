from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import BookData


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer