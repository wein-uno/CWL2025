   from django.urls import path, include   
   from rest_framework import viewsets
   from .views import DogViewSet, BreedViewSet

   router = DefaultRouter()
   router.register(r'comics', ComicsViewSet)
   
   urlpatterns = [
       path('', include(router.urls)),
   ]



