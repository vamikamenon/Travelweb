from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method == 'POST':
        uname = request.POST['User_Name']
        fname = request.POST['First_Name']
        lname = request.POST['Last_Name']
        email = request.POST['Email']
        pwd = request.POST['Password']
        cpwd = request.POST['Password1']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "User Name Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Id already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=email)
                user.save()
                # messages.info(request, "Registered Successfully")
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['User_Name']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"User not registered/Incorrect credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

