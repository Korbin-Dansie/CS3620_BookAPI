"""
URL configuration for BookAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from books.views import BiographyViewSet, CookbookViewSet, FictionViewSet, HistoryViewSet, HumorViewSet, NonfictionViewSet, PoetryViewSet, RatingViewSet, RomanceViewSet, home_view, BookViewSet, FantasyViewSet

# Set up a router for the REST api
# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register("books", BookViewSet) # Set up urls at ~/books/
router.register("fantasy", FantasyViewSet)
router.register("fiction", FictionViewSet)
router.register("romance", RomanceViewSet)
router.register("humor", HumorViewSet)
router.register("nonfiction", NonfictionViewSet)
router.register("biography", BiographyViewSet)
router.register("history", HistoryViewSet)
router.register("poetry", PoetryViewSet)
router.register("cookbook", CookbookViewSet)
router.register("rating", RatingViewSet)

urlpatterns = [
    path('', home_view, name='home'), # Change the index page
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
