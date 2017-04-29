from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def login(self, postData):
        data = {
            'valid': False,
            'errors': []
        }
        if not postData:
            return data
        if len(postData['email']) < 2 or len(postData['password']) < 2:
                data['errors'].append("email and password cannot be blank")
                return data
        if User.objects.filter(email = postData['email']).exists():
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode('utf_8'), user.password.encode('utf_8')):
                data['valid'] = True
                data['user'] = user
                return data
            else:
                data['errors'].append('password is not correct')
                return data
        else:
            data['errors'].append("email not valid")
            return data
    def register(self, postData):
        data = {
            'valid': False,
            'errors': []
        }
        # check if there is post data
        if not postData:
            return data
        if len(postData['name']) < 2:
            data['errors'].append('Name must be at least 3 characters')
        else:
            if not postData['name'].replace(' ', '').isalpha():
                data['errors'].append("Name must be letters only")
        if len(postData['alias']) < 2:
            data['errors'].append('Alias must be at least 2 characters')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            data['errors'].append('invalid email')
        if User.objects.filter(email = postData['email']).exists():
            data['errors'].append("email already registered. Try logging in...")
        if postData['password'] != postData['password-confirmation']:
            data['errors'].append("passwords don't match")
        if len(postData['password']) < 8:
            data['errors'].append("password must be at least 8 characters")
        if data['errors']:
            return data
        else:
            user = User.objects.create(name = postData['name'], alias = postData['alias'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode('utf_8'), bcrypt.gensalt()))
            data['user'] = user
            data['valid'] = True
            return data

class User(models.Model):
    name = models.TextField(max_length=100)
    alias = models.TextField(max_length = 100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()