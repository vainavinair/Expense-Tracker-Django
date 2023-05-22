from django.urls import path 
from .views import index_view, expense_chart_data

urlpatterns = [
    path('', index_view, name='chart'),
     path('expense-chart-data/', expense_chart_data, name='expense-chart-data')
]