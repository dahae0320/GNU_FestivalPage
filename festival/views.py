from django.shortcuts import render

# Create your views here.

def foodtruck(request):
    return render(request, 'foodtruck.html')
    
def index(request):
    return render(request, 'index.html')

def scprogram(request):
    return render(request, 'sc_program.html')
    
def singer(request):
    return render(request, 'singer.html')
