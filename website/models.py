from django.db import models
from newapp.models import addcategorydb,productdb


# Create your models here.
class contactdb(models.Model):
    name=models.CharField(max_length=60,null=True,blank=True)
    email=models.CharField(max_length=60,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=200,null=True,blank=True)
class singupdb(models.Model):
    username=models.CharField(max_length=60,null=True,blank=True)
    email=models.CharField(max_length=60,null=True,blank=True)
    password=models.CharField(max_length=60,null=True,blank=True)
    re_password=models.CharField(max_length=60,null=True,blank=True)
class Cart(models.Model):
    productname = models.CharField(max_length=60,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(null=True,blank=True)
class cartmodel(models.Model):
    productname = models.CharField(max_length=60, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=60, null=True, blank=True)
class buycart(models.Model):
    productnm = models.CharField(max_length=60, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)
    user = models.CharField(max_length=60, null=True, blank=True)
    firstname= models.CharField(max_length=60, null=True, blank=True)
    lastname = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    address= models.CharField(max_length=200, null=True, blank=True)
class admincart(models.Model):
    productnm = models.CharField(max_length=60, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)
    user = models.CharField(max_length=60, null=True, blank=True)
    firstname = models.CharField(max_length=60, null=True, blank=True)
    lastname = models.CharField(max_length=60, null=True, blank=True)
    country = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    dataid = models.IntegerField(null=True, blank=True)








