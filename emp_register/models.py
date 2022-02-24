from django.db import models

# Create your models here.

class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
