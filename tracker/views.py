import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    # api_key = os.environ['API_KEY']
    # print (api_key)
    return render(request, 'tracker/home.html')

def error_view(request):
    return render(request, 'tracker/error.html')
