
from django.db import models

# Create your models here.

class Users(models.Model):
    pseudo = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250,)
    created_at = models.DateField(auto_now_add=True)


