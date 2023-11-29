from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('attend/', views.index, name='index'),
    path('users/', views.details, name='details'),
    path('atndnc/', views.index1, name='index1'),
    path('dtls', views.details1, name='details1'),
    path('process/', views.process, name = 'process')
]