from django.shortcuts import render
from django.contrib.auth import get_user_model
from math import ceil
User=get_user_model()

def Profile_View(request,username):
    if request.user==username:
        user=request.user
    else:
        user=User.objects.get(username=username)

    profile=user.profile_set.all()
    ads=user.product_set.all()

    return render(request,'Profile/profile.html',{'user':user,'profile':profile,'product':ads,})

