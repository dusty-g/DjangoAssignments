from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
class Messages(models.Model):
    user = models.ForeignKey('Users')
    message = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comments(models.Model):
    message = models.ForeignKey('Messages')
    user = models.ForeignKey('Users')
    comment = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

