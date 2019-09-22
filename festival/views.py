from django.shortcuts import render


def scprogram(request):
    return render(request, 'sc_program.html')