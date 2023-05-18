import os
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Expense
from .forms import ExpenseForm


@login_required
def home_view(request):
    form = ExpenseForm(request.POST or None)
    # api_key = os.environ['API_KEY']
    # print (api_key)
    expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'expenses': expenses,
        'form': form
    }
    return render(request, 'tracker/home.html', context)


def save_expense(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            user = request.user  
            form.instance.user = user
            form.save()
            data['form_is_valid'] = True
            expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
            data['table_html'] = render_to_string('tracker/expense_table.html',{'expenses': expenses})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context,request=request)
    return JsonResponse(data)

def create_view(request):
    form = ExpenseForm(request.POST or None)
    return save_expense(request,form,'tracker/create_form.html')
    

def update_view(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
    else:
        form = ExpenseForm(instance=expense)
    return save_expense(request,form,'tracker/update_form.html')

def delete_view(request,id):
    expense = get_object_or_404(Expense, id=id)
    data = dict()
    if request.method == 'POST':
        if request.user == expense.user:
            expense.delete()
            data['form_is_valid'] = True
            expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
            data['table_html'] = render_to_string('tracker/expense_table.html',{'expenses': expenses})
    else:
        context = {
            'obj':expense
        }
        data['html_form'] = render_to_string('tracker/delete_confirm.html',context,request=request)
    return JsonResponse(data)

def error_view(request):
    return render(request, 'tracker/error.html')