from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('scprogram/',views.scprogram, name='scprogram'),
    path('foodtruck/',views.foodtruck, name='foodtruck'),
    path('singer/', views.singer, name='singer'),
=======
    path('', views.scprogram, name='scprogram')
>>>>>>> studentprogram
]