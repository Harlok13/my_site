from django.db import models

class SalesOrder(models.Model):
    amounts = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=False)

