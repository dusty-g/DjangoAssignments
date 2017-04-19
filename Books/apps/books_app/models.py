from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40)
    published = models.IntegerField()
    in_print = models.BooleanField()
    category = models.CharField(max_length = 30)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
