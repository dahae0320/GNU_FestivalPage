from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scprogram/',views.scprogram, name='scprogram'),
    path('foodtruck/',views.foodtruck, name='foodtruck'),
]