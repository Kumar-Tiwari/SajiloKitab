from django.shortcuts import render,redirect
from .forms import Signup_Form
from django.contrib import messages

def Signup_View(request):
    try:
        key=request.session['member-id']
        return redirect('/home/')
    except:
        if request.method=="POST":
            form=Signup_Form(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.set_password(user.password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Account Created successfully')
                return redirect('/')
            else:
                form=Signup_Form(request.POST)
                return render(request,'Signup/signup.html',{"form":form})
        else:
            form=Signup_Form()
            return render(request,'Signup/signup.html',{"form":form})

