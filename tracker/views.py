import os
from django.contrib import messages 

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

def get_sum(request):
    debit_sum = Expense.objects.filter(transaction_type__name='Debit', user=request.user).aggregate(sum=Sum('amount'))['sum'] or 0
    credit_sum = Expense.objects.filter(transaction_type__name='Credit', user=request.user).aggregate(sum=Sum('amount'))['sum'] or 0
    difference = credit_sum + debit_sum
    sum_data = {
        'debit_sum': debit_sum,
        'credit_sum': credit_sum,
        'difference': difference
    }
    return sum_data

    

@login_required
def home_view(request):
    form = ExpenseForm(request.POST or None)
    expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'expenses': expenses,
        'form': form,
        'sum_data': get_sum(request),
    }
    return render(request, 'tracker/home.html', context)



def save_expense(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            user = request.user  
            form.instance.user = user
            if form.instance.transaction_type.name == 'Debit':
                form.instance.amount = -form.instance.amount
            form.save()
            data['form_is_valid'] = True
            expenses = Expense.objects.filter(user=request.user).order_by('-created_at')
            data['table_html'] = render_to_string('tracker/expense_table.html',{'expenses': expenses})
            data['sums_html'] = render_to_string('tracker/sums.html',{'sum_data': get_sum(request)})
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
            data['sums_html'] = render_to_string('tracker/sums.html',{'sum_data': get_sum(request)})
    else:
        context = {
            'obj':expense
        }
        data['html_form'] = render_to_string('tracker/delete_confirm.html',context,request=request)
    return JsonResponse(data)

def error_view(request):
    return render(request, 'tracker/error.html')