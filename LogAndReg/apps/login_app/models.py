from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        errors = []
        data = {
            'valid': False,
            'errors': errors,
        }
        
        if not postData:
            errors.append("post only!")
            return data
        else:
            if len(postData['email']) < 2 or len(postData['password']) < 2:
                errors.append("email and password cannot be blank")
                return data
            else:
                if User.objects.filter(email = postData['email']).exists():
                    user = User.objects.get(email = postData['email'])
                    if user.password == postData['password']:
                        data['valid'] = True
                        data['user'] = user
                        return data
                    else:
                        errors.append("password is not correct")
                        return data
                else:
                    errors.append("user does not exist")
                    return data
    
    
    def register(self, postData):
        errors = []
        data = {
            'valid': False,
            'errors': errors,
        }
        if not postData:
            errors.append("post only!")
            return data
        if len(postData['first-name']) < 2 or len(postData['last-name']) < 2:
            errors.append("First and Last name must be 2 or more characters")
        # if not postData['first-name'].isalpha() or postData['last-name'].isalpha():
            # errors.append('first and last name must be letters only')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            errors.append('invalid email')
        if User.objects.filter(email = postData['email']).exists():
            errors.append("email already registered. Try logging in...")
        if postData['password'] != postData['password-confirmation']:
            errors.append("passwords don't match")
        if len(postData['password']) < 4:
            errors.append("password must be at least 4 characters")
        if errors:
            return data
        else:
            user = User.objects.create(first_name = postData['first-name'], last_name = postData['last-name'], email = postData['email'], password = postData['password'])
            data['user'] = user
            data['valid'] = True
            return data
        
class User(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length = 100)
    email = models.TextField(max_length=100)
    password = models.TextField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()