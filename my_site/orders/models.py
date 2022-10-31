from django.contrib.auth.models import User
from django.db import models

class SalesOrder(models.Model):
    amount = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

