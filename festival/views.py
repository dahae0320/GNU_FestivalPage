from django.shortcuts import render

# Create your views here.

def foodtruck(request):
    return render(request, 'foodtruck.html')