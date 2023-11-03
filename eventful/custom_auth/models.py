# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ishost = models.BooleanField(default=False) 

    def __str__(self):
        return self.username
