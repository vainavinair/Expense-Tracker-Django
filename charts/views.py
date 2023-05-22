from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from tracker.models import Expense


def index_view(request):
    return render(request,'charts/index.html')

def expense_chart_data(request):
    expense_data = Expense.objects.values('category__name').annotate(total_amount=Sum('amount'))
    return JsonResponse(list(expense_data), safe=False)