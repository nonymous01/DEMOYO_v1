from django.db import models

# Create your models here.
# python manage.py runserver
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique =True)
    password=models.CharField(max_length=200)
