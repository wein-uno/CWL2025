from django.urls import path, include   
from rest_framework.routers import DefaultRouter
from .views import ComicsViewSet

router = DefaultRouter()
router.register(r'comicsapi', ComicsViewSet)
   
urlpatterns = [
    path('', include(router.urls)),
    ]



