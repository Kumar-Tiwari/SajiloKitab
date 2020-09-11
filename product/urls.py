from django.urls import path
from .views import Product_View
urlpatterns = [ 
    path('product',Product_View,name='product'),
]