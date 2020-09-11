from django.shortcuts import render,redirect
from .forms import DocumentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User=get_user_model()


@login_required
def Product_View(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.author=request.user
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

    return render(request, 'product/product.html', {'form': form})
