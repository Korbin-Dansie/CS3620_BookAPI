from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import BookData


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html") # return an html template


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "fantasy")
    serializer_class = BookSerializer

class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "fiction")
    serializer_class = BookSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "romance")
    serializer_class = BookSerializer

class HumorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "humor")
    serializer_class = BookSerializer

class NonfictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "nonfiction")
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "biography")
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "history")
    serializer_class = BookSerializer

class PoetryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "poetry")
    serializer_class = BookSerializer

class CookbookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category = "cookbook")
    serializer_class = BookSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(rating__gte = 4)
    serializer_class = BookSerializer