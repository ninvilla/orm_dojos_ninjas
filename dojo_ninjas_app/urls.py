from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/create', views.dojo),
    path('ninja/create', views.ninja)
]