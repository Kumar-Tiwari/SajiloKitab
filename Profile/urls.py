from django.urls import path
from .views import Profile_View
urlpatterns = [ 
    path('',Profile_View,name='profile')
]