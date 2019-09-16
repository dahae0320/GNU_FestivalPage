from django.urls import path
from . import views

urlpatterns = [
    path('studentprogram/', views.scprogram, name='scprogram')
]