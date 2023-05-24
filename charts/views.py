from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Sum
from tracker.models import Expense


def index_view(request):
    labels = []
    data = []
    queryset = Expense.objects.filter(Q(amount__lt=0)&Q(user=request.user))
    for expense in queryset:
        labels.append(expense.title)
        data.append(abs(expense.amount))
    return render(request, 'charts/index.html', {
        'labels': labels,
        'data': data,
    })

def expense_chart_data(request):
    expense_data = Expense.objects.values('category__name').annotate(total_amount=Sum('amount'))
    return JsonResponse(list(expense_data), safe=False)
