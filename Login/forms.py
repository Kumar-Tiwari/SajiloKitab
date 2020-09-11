from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class Login_Form(forms.ModelForm):
    password=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))
    username=forms.CharField(max_length=16,widget=forms.TextInput(attrs={
        "placeholder":"Username"
    }))
    class Meta:
        model=User
        fields=['username','password']