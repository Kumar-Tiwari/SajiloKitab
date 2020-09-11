from django import forms
from .models import Product
 
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['in_stock','Images','author','slug']
