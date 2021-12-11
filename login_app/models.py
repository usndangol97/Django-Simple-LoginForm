from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class custom_user(models.Model):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(max_length=100,  null=True)
    password = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name