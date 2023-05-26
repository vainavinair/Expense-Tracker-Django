from django.urls import path
from .views import register,token_send, verify,error_page, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='user-register'),
    path('login/', CustomLoginView.as_view(), name="user-login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
    path('token/',token_send, name='user-token'),
    path('verify/<auth_token>',verify, name='verify'),
    path('error/',error_page, name='error-page'),
]
