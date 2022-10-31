from django.db import models

class Solo(models.Model):
    name = models.CharField(max_length=100)
