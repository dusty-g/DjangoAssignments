from __future__ import unicode_literals

from django.db import models


class noteManager(models.Manager):
    def addNote(self, postData):
        if postData:
            if len(postData['note']) == 0:
                return False
            else:
                Note.objects.create(note = postData['note'])
                return True
        else:
            return False
# Create your models here.
class Note(models.Model):
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = noteManager()