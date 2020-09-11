from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from math import ceil

@login_required()
def Home_View(request):
    allProducts=[]
    category_prods=Product.objects.values('category','id')
    cats={item['category'] for item in category_prods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        length=len(prod)
        sildes=length//4 + ceil(length/4-length//4)
        allProducts.append([prod,range(1,sildes),sildes])
    context={
        'allProds':allProducts,
    }
    return render(request,'Home/home.html',context)
