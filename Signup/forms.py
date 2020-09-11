from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()

class Signup_Form(forms.ModelForm):
    confirm_password=forms.CharField(max_length=26,error_messages={"match":"Password didn't match"},widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password"
    }))
    password=forms.CharField(max_length=26,widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))
    username=forms.CharField(max_length=26,error_messages={"unique":"Username is already taken"},widget=forms.TextInput(attrs={
        "placeholder":"Username"
    }))
    email=forms.CharField(max_length=26,widget=forms.EmailInput(attrs={
        "placeholder":"Email Address"
    }))
    first_name=forms.CharField(max_length=26,widget=forms.TextInput(attrs={
        "placeholder":"First Name"
    }))
    last_name=forms.CharField(max_length=26,widget=forms.TextInput(attrs={
        "placeholder":"Last Name"
    }))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
    
    def clean_confirm_password(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']

        if password != confirm_password :
            raise forms.ValidationError("Password not matched")

        else:
            return confirm_password
        