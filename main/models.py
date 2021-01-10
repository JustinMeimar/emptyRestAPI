from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=None)
    message = models.TextField(max_length=400, blank=False)
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default=None)
    message = models.CharField(max_length=400)
