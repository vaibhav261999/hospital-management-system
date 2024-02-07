from django.db import models

# Create your models here.
class AdminRegister(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    userName=models.CharField(max_length=20)
    Contact=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class Dr_Register(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    userName=models.CharField(max_length=20)
    Contact=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)

class Patient_Register(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    Contact=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=20)
    Symptoms=models.CharField(max_length=50)


    
