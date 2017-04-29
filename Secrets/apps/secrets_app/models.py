from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

class SecretManager(models.Manager):
    def addSecret(self, postData):
        data = {
            'valid': False,
            'errors': []
        }
        if postData:
            
            if len(postData['secret'])< 2:
                data['errors'].append('secret must be at least 2 characters')
            else:
                user = User.objects.get(id = int(postData['user']))
                newSecret = self.create(user = user, secret = postData['secret'])
                data['valid'] = True
            return data
    
    

        

class Secret(models.Model):
    user = models.ForeignKey(User, related_name='secrets')
    secret = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='likes')

    objects = SecretManager()