from django.shortcuts import render

# Create your views here.

def foodtruck(request):
    return render(request, 'foodtruck.html')
    
def index(request):
    return render(request, 'index.html')
