from django import forms

from tracker.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']