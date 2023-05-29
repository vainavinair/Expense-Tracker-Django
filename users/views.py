import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .forms import UserCreateForm
from .models import UserProfile


def send_mail_otp(email,token):
    subject = "Email verification"
    message = f'Click this link to verify your account http://localhost:8000/users/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email=email_from, recipient_list=recipient_list)

def verify(request, auth_token):
    try:
        profile_obj = UserProfile.objects.filter(auth_token=auth_token).first()
        if not profile_obj.verification:
            profile_obj.verification=True
            profile_obj.save() 
            messages.success(request,f"Account has been verified. Welcome to SpendWise {profile_obj.username}!")
            return redirect('user-login')
        else:
            messages.success(request,f"Account has been verified already")
            return redirect('user-login')
    except:
        return redirect('error-page')
    
def error_page(request):
    return render (request, 'users/error.html')

def token_send(request):
    return render(request,'users/token.html')

def register(request):
    form = UserCreateForm(request.POST or None)
    if request.method == "GET":
        context = {
            'form': form,
        }
        return render(request, "users/register.html",context)
    elif request.method == "POST":
        if form.is_valid():
            email=form.cleaned_data.get('email')
            user = form.save()
            token=str(uuid.uuid4())
            user_profile_obj = UserProfile.objects.create(username=user, auth_token=token)
            user_profile_obj.save()
            send_mail_otp(email,token)
            messages.success(request,f"Account created !")
            return redirect("user-token")
        

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    def form_valid(self, form):
        user = form.get_user()
        user_obj = UserProfile.objects.filter(username=user).first()
        if  user_obj.verification:
            return super().form_valid(form)
        messages.error(self.request, 'Your account is not verified yet.')
        return redirect('user-login')