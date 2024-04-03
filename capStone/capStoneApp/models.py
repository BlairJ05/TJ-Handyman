from django.db import models
from datetime import datetime

class Message(models.Model):
    value = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)