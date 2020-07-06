from django.urls import path
from . import views

urlpatterns = [
    path('Home',views.base, name='base'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('index',views.index, name='index'),


]