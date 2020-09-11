from django.urls import path
from .views import Detail_View
urlpatterns = [
    path('',Detail_View,name='detail'),
]