from django.shortcuts import render

# Create your views here.
def singer(request):
    return render(request, 'singer.html')