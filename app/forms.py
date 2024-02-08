from django import forms
from .models import *

class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model=AdminRegister
        fields='__all__'

class Dr_RegisterForm(forms.ModelForm):
    class Meta:
        model=Dr_Register
        fields='__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient_Register
        fields='__all__'



class Book_AppointmentForm(forms.ModelForm):
    class Meta:
        model=Book_Appointment
        fields='__all__'



        