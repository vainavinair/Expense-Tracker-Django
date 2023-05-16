from django.shortcuts import render

def home_view(request):
    return render(request, 'tracker/home.html')

def error_view(request):
    return render(request, 'tracker/error.html')
    