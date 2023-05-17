import os
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Expense
from .forms import CreateExpenseForm


@login_required
def home_view(request):
    form = CreateExpenseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = request.user  # Assuming you want to use the currently logged-in user
            form.instance.user = user
            form.save()
            return HttpResponse("good request")

    elif request.method == 'GET':
        # api_key = os.environ['API_KEY']
        # print (api_key)
        context = {
            'expenses': Expense.objects.filter(user=request.user).order_by('-created_at'),
            'form': form
        }
        return render(request, 'tracker/home.html', context)


def error_view(request):
    return render(request, 'tracker/error.html')
