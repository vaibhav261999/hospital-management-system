from django.urls import path

from .views import *

urlpatterns = [
   path('',base,name="base"),

    path('SignUp/', SignUp, name='SignUp'),

    path('RegisterForm/<str:pk>', RegisterForm, name='RegisterForm'),
    path('Register/<str:pk>', Register, name='Register'),
    path('loginForm/<str:pk>', loginForm, name='loginForm'),
    path('Login/<str:pk>', Login, name='Login'),

]
