from django.shortcuts import render
from product.models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User=get_user_model()

@login_required()
def Detail_View(request,slug):

    try:
        detail=Product.objects.get(slug=slug)
        author=detail.author.profile_set.all()
    except:
        pass

    return render(request,'Detail/detail.html',{'detail':detail,'author':author})