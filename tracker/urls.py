from django.urls import path 
from .views import home_view, error_view

urlpatterns = [
    path('', home_view, name='tracker-home'),
    path('error/', error_view, name='error'),
]