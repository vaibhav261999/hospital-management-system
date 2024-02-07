from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def base(request):
    return render(request,'app/base.html')
# -------------------------------------------------

def SignUp(request):
    return render(request,'app/SignUp.html')

def RegisterForm(request,pk):
    if pk=="admin":
        Admin_form=AdminRegisterForm()
        
        return render(request,'app/RegisterForm.html',{'Admin_form':Admin_form})
    
    elif pk=="dr":
        Dr_form=Dr_RegisterForm()
        return render(request,'app/RegisterForm.html',{'Dr_form':Dr_form})
    else:
        patient_form=PatientForm()
        return render(request,'app/RegisterForm.html',{'patient_form':patient_form})

def Register(request,pk):
    if request.method=="POST":
        if pk=="admin":
            fname =request.POST['firstName'] 
            lname =request.POST['lastName'] 
            username = request.POST['userName']
            contact =request.POST['Contact'] 
            email =request.POST['Email'] 
            Password = request.POST['Password']

            valid=AdminRegister.objects.filter(Email=email)
            if valid:
                msg="Admin already exist"
                return render(request,'app/SignUp.html',{'Amsg':msg})
                
            else:
                AdminRegister.objects.create(
                            firstName=fname, 
                            lastName=lname, 
                            userName=username, 
                            Contact=contact, 
                            Email=email, 
                            Password=Password )

                msg="Admin Ragister Successfully"
                return render(request,'app/SignUp.html',{'Amsg':msg})
        
        elif pk=="dr":
            fname=request.POST['firstName']
            lname=request.POST['lastName']
            username=request.POST['userName']
            contact=request.POST['Contact']
            email=request.POST['Email']
            Password=request.POST['Password']

            valid=Dr_Register.objects.filter(Email=email)
            if valid:
                msg="Doctor already exist"
                return render(request,'app/SignUp.html',{'Dmsg':msg})
            else:
                Dr_Register.objects.create(
                            firstName=fname, 
                            lastName=lname, 
                            userName=username, 
                            Contact=contact, 
                            Email=email, 
                            Password=Password)
                msg="Doctor Ragister Successfully"
                return render(request,'app/SignUp.html',{'Dmsg':msg})
        
        elif pk=="patient":
            fname=request.POST['firstName']
            lname=request.POST['lastName']
            contact=request.POST['Contact']
            email=request.POST['Email']
            password=request.POST['Password']
            symptoms=request.POST['Symptoms']

            valid=Patient_Register.objects.filter(Email=email)
            if valid:
                msg="Patient already exist"
                return render(request,'app/SignUp.html',{'Pmsg':msg})
            
            else:
                Patient_Register.objects.create(
                    firstName=fname,
                    lastName=lname,
                    Contact=contact,
                    Email=email,
                    Password=password,
                    Symptoms=symptoms)
                msg="Patient Ragister Successfully"
                return render(request,'app/SignUp.html',{'Pmsg':msg})
            
    else:
        msg="Request Method is not 'POST' "
        return render(request,'app/SignUp.html',{'msg':msg})

def loginForm(request,pk):
    if pk=="admin":
        msg='admin'
        return render(request,'app/logIn.html',{"admin":pk})

    
    elif pk=="dr":
        msg='dr'
        return render(request,'app/logIn.html',{'dr':msg})
    
    else:
        msg='patient'
        return render(request,'app/logIn.html',{'patient':msg})

    
  

def Login(request,pk):
    if request.method=="POST":
        if pk=="admin":
            email=request.POST['email']
            password=request.POST['password']

            valid=AdminRegister.objects.filter(Email=email)
            if valid:
                data=AdminRegister.objects.get(Email=email)
                if password==data.Password:

                    fname=data.firstName
                    lname=data.lastName
                    user=data.userName
                    contact=data.Contact
                    email=data.Email
                    password=data.Password

                    AdminData={
                        'fname':fname,
                        'lname':lname,
                        'user':user,
                        'contact':contact,
                        'email':email,
                        'password':password,
                    }
                    msg="Admin log-In Successfully"
                    return render(request,'app/dashboard.html',{'Data':AdminData,'msg':msg})
                else:
                    msg="Incorrect Password"
                    return render(request,'app/logIn.html',{"admin":pk,'msg':msg})

            else:
                msg="Incorrect Email"
                return render(request,'app/logIn.html',{"admin":pk,'msg':msg})
# --------------------------------
        elif pk=='dr':
            email=request.POST['email']
            password=request.POST['password']

            valid=Dr_Register.objects.filter(Email=email)
            if valid:
                data=Dr_Register.objects.get(Email=email)
                if password==data.Password:

                    fname=data.firstName
                    lname=data.lastName
                    user=data.userName
                    contact=data.Contact
                    email=data.Email
                    password=data.Password

                    Dr_Data={
                        'fname':fname,
                        'lname':lname,
                        'user':user,
                        'contact':contact,
                        'email':email,
                        'password':password,
                    }
                    msg=" Doctor log-In Successfully"
                    return render(request,'app/dashboard.html',{'Data':Dr_Data,'msg':msg})
                else:
                    msg="Incorrect Password"
                    return render(request,'app/logIn.html',{"dr":pk,'msg':msg})

            else:
                msg="Incorrect Email"
                return render(request,'app/logIn.html',{"dr":pk,'msg':msg})
#  --------------------------------
        else:
            email=request.POST['email']
            password=request.POST['password']

            valid=Patient_Register.objects.filter(Email=email)
            if valid:
                data=Patient_Register.objects.get(Email=email)
                if password==data.Password:

                    fname=data.firstName
                    lname=data.lastName
                    contact=data.Contact
                    email=data.Email
                    password=data.Password
                    symp=data.Symptoms

                    Patient_Data={
                        'fname':fname,
                        'lname':lname,
                        'contact':contact,
                        'email':email,
                        'password':password,
                        'symptoms':symp,
                    }
                    msg=" Patient log-In Successfully"
                    return render(request,'app/dashboard.html',{'Data':Patient_Data,'msg':msg})
                else:
                    msg="Incorrect Password"
                    return render(request,'app/logIn.html',{"dr":pk,'msg':msg})

            else:
                msg="Incorrect Email"
                return render(request,'app/logIn.html',{"patient":pk,'msg':msg})            



    else:
        msg="Request Method is not 'POST' "
        return render(request,'app/logIn.html',{'msg':msg})




