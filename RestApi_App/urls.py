from django.urls import path, include
from . import views
from .views import ModelViewSet 

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('RestApi',ModelViewSet, basename='RestApi')


urlpatterns = [

        path('',include(router.urls)),
                 
        ]
 