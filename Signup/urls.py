from django.urls import path
from .views import Signup_View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create', Signup_View,name="signup"),

] 