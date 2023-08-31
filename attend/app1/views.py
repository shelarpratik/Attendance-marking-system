from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
#from django.views.generic import FormView
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

def homepage(request):
    return render(request,'mainpage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if username is None:
            login(request, user)

        else:
            messages.error(request, "Bad input!!!")
            return redirect("homepage") 

    return render(request,'stulogin.html')   

def reg(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST[ 'email']
        password = request. POST[ 'password']
        confirm_password = request.POST['confirm_password']
        
        myuser = User.objects.create_user(username,email,password,confirm_password)
        myuser.username = username
        myuser.email = email
        
        myuser.save()

        messages.success(request, "Account Created Successfully...")
        return redirect('stulogin')
    return render(request,'stureg.html')