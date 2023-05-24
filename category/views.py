from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages 
from tracker.models import Category
from .forms import CategoryForm
# Create your views here.


def category_view(request):
    categories = Category.objects.filter(Q(user=request.user) | Q(user=User.objects.get(id=1)))
    form = CategoryForm(request.POST or None)
    context = {
        'categories': categories,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            user = request.user  
            form.instance.user = user
            form.save()
            return redirect('tracker-home')
    elif request.method == 'GET':
        pass
    return render(request, 'category/category_page.html', context)


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.user == category.user:
        category.delete()    
        return redirect(reverse('category'))

    messages.error(request, "Default categories cannot be deleted" )
    return redirect(reverse('category'))