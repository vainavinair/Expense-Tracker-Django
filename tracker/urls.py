from django.urls import path 
from .views import home_view, error_view, delete_view, update_view

urlpatterns = [
    path('', home_view, name='tracker-home'),
    path('error/', error_view, name='error'),
    path('<int:id>/update/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
]