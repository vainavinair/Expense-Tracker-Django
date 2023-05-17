import os
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
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
            return redirect('tracker-home')
        else:
            return redirect('tracker-home')
        
    elif request.method == 'GET':
        # api_key = os.environ['API_KEY']
        # print (api_key)
        expenses = Expense.objects.filter(user=request.user).order_by('-created_at')

        context = {
            'expenses': expenses,
            'form': form
        }
        return render(request, 'tracker/home.html', context)


def error_view(request):
    return render(request, 'tracker/error.html')


# def update_view(request,id):
#     expense = get_object_or_404(Expense, id=id)
#     if request.user == expense.user:
#         if request.method=="POST":
#             pass
#         else:
#             form = CreateExpenseForm(instance=expense)
#             pass
#     else:
#         return HttpResponseForbidden()


def delete_view(request,id):
    expense = get_object_or_404(Expense, id=id)
    if request.user == expense.user:
        expense.delete()
        return redirect('tracker-home')
    else: 
        return redirect('blog-home')

    