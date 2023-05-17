from django import forms
from .models import Expense

class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = (
            'title',
            'description',
            'amount',
            'category'
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2})
        }