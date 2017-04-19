from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 38)
    description = models.TextField()
    weight = models.FloatField()
    price = models.DecimalField(max_digits= 4, decimal_places=2)
    cost = models.DecimalField(max_digits= 4, decimal_places=2)
    category = models.CharField(max_length = 32)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
