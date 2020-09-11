from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse 
from django.template.defaultfilters import slugify

User=get_user_model()

CATEGORY_BOOKS = (
    ('School Level','School Level'),
    ('Bachelor Level','Bachelor Level',),
    ('Entertainment','Entertainment'),
    ('Other','Other')

)
# class Category(models.Model):
#     title=models.CharField(max_length=2)

class Product(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(default='',max_length=20,null=True,unique=True)
    title=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    category=models.CharField(choices=CATEGORY_BOOKS,max_length=20,default='Other')
    in_stock=models.BooleanField(default=True)
    feature_image=models.ImageField(upload_to='product',blank=True,default='product/output-onlinepngtools_4_m0DaNEc.png')
    Images=models.ImageField(upload_to='product',blank=True,null=True)
    # created_on=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title