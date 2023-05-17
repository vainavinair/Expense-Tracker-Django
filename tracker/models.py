from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return self.title