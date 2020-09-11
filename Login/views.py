from django.shortcuts import render,redirect
from .forms import Login_Form
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as lgn
from django.contrib.auth import logout
from django.contrib import messages

def Login_View(request):
    try:
        key=request.session['member-id']
        return redirect('/home/')
    except:
        if request.method=="POST":
            form=Login_Form(request.POST)
            username=request.POST['username']
            password=request.POST['password']
            user=auth(username=username,password=password)
            if user is not None:
                lgn(request,user)
                request.session['member-id']=user.id
                return redirect('/home/')
            else:
                return render(request,"Login/login.html",{'form':form , 'error':'True'})

        else:
            form=Login_Form()
            return render(request,"Login/login.html",{'form':form})

def Logout_View(request):
    del request.session['member-id']
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
