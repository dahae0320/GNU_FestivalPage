from django.urls import path
from . import views

urlpatterns = [
    path('foodtruck/',views.foodtruck, name='foodtruck'),
]