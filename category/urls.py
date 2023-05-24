from django.urls import path
from . views import category_view, delete_category

urlpatterns = [
    path('', category_view, name='category'),
    path('delete/<int:id>', delete_category, name='delete_category'),
]