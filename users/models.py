from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    verification = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)