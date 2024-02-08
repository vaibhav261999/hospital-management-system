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


class Book_Appointment(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    dob=models.CharField(max_length=50)
    general=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=20)    
    address=models.CharField(max_length=20)    
    email=models.EmailField()    
    doctor_name=models.CharField(max_length=20)    


