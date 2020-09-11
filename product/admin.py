from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display =[ 'author','slug','title','description','price','category','in_stock','feature_image','Images']
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Product, ProductAdmin)