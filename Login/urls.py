from django.urls import path
from .views import Login_View,Logout_View
urlpatterns = [ 
    path('',Login_View,name='login'),
    path('logout',Logout_View,name='logout'),
]