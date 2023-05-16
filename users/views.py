from django.shortcuts import render, redirect

from .forms import UserCreateForm

def register(request):
    form = UserCreateForm(request.POST or None)
    if request.method == "GET":
        context = {
            'form': form,
        }
        return render(request, "users/register.html",context)
    elif request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("tracker-home")