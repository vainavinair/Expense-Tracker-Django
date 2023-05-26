from django.db.models import Sum,Q
from django.shortcuts import render
from django.contrib.auth.models import User

from tracker.models import Category, Expense

def index_view(request, id):
    debit_labels = []
    debited_amt = []
    credited_labels = []
    credited_amt = []
    category_lables=[]
    category_sums=[]
    category_lables2=[]
    category_sums2=[]
    

    debited = Expense.objects.filter(Q(amount__lt=0) & Q(user=request.user))
    credited = Expense.objects.filter(Q(amount__gt=0) & Q(user=request.user))

    debit_expense_categories = Category.objects.filter(Q(expense__amount__lt=0) & Q(expense__user=request.user))
    debit_category_sums = debit_expense_categories.annotate(total_amount=Sum('expense__amount')).values('name', 'total_amount')

    credit_expense_categories = Category.objects.filter(Q(expense__amount__gt=0) & Q(expense__user=request.user))
    credit_category_sums = credit_expense_categories.annotate(total_amount=Sum('expense__amount')).values('name', 'total_amount')

    for expense in debited:
        debit_labels.append(expense.title)
        debited_amt.append(abs(expense.amount))

    for expense in credited:
        credited_labels.append(expense.title)
        credited_amt.append(abs(expense.amount))

    for category_sum in debit_category_sums:
        category_lables.append(category_sum['name'])
        category_sums.append(abs(category_sum['total_amount']))

    for category_sum in credit_category_sums:
        category_lables2.append(category_sum['name'])
        category_sums2.append(abs(category_sum['total_amount']))
    

    return render(request, 'charts/charts.html', {
        'debit_labels': debit_labels,
        'debited_amt': debited_amt,
        'credited_labels': credited_labels,
        'credited_amt': credited_amt,
        'category_lables':category_lables,
        'category_sums':category_sums,
        'category_lables2':category_lables2,
        'category_sums2':category_sums2
    })
