from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            'title',
            'description',
            'amount',
            'category',
            'transaction_type'
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2})
        }

