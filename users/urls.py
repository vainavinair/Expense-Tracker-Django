from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='user-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
]
