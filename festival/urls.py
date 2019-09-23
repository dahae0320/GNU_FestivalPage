from django.urls import path
from . import views

urlpatterns = [
    path('scprogram/', views.scprogram, name='scprogram')
]