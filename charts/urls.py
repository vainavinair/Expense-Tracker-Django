from django.urls import path 
from .views import index_view

urlpatterns = [
    path('<id>/', index_view, name='user-profile'),
]