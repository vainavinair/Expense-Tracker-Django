from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class TransactionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return self.title