from django.urls import path
from . import views

urlpatterns = [
    path('singer/', views.singer, name='singer'),
]