from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.TextField(max_length=220)
    author = models.TextField(max_length=220)
    category = models.TextField(max_length=220)