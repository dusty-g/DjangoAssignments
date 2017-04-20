from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def login(self, postData):
        errors = []
        data = {
            'valid': False,
            'errors': errors,
        }
        if not postData:
            print "not postdata"
            errors.append("post only!")
            return data
        if len(postData['username']) <1:
            errors.append("name cannot be blank")
        if User.objects.filter(username = postData['username']).exists():
            errors.append("username already exists")
        if errors:
            data['valid'] = False
        else:
            data['valid'] = True
            
            data['newuser'] = User.objects.create(username = postData['username'])
        
        return data

class User(models.Model):
    username = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()