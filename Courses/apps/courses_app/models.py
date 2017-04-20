from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.TextField(max_length=45)
    description = models.TextField(max_length=255)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

# class Descriptions(models.Model):
    
#     course = models.ForeignKey(Courses)