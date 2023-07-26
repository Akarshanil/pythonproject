from django.db import models

# Create your models here.
class addcategorydb(models.Model):
    categoryname=models.CharField(max_length=70,null=True,blank=True)
    image=models.ImageField(upload_to="profile")
    description=models.CharField(max_length=70,null=True,blank=True)
class productdb(models.Model):
    selectcategory = models.CharField(max_length=100, null=True, blank=True)
    productname = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField( null=True, blank=True)
    price = models.IntegerField( null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=productname, null=True, blank=True)
