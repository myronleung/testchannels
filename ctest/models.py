from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length = 200, default = '')

class UserProfile(models.Model):
    username = models.CharField(max_length = 20, default = 'default')

class Message(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
