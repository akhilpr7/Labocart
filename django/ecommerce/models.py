from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

class ProductsModel(models.Model):
    Product_name = models.TextField(max_length=100,null=False, blank=False)
    Price = models.FloatField(max_length=20,null=False, blank=False)
    Quantity = models.IntegerField(null=False,blank=False,)
    Image = models.ImageField(upload_to='product',blank=False,null=False)
    def __str__(self):
        return self.Product_name

class CartModel(models.Model):
    product_id = models.IntegerField(blank=False,null=False)
    Product_name = models.TextField(max_length=100, blank=False,null=False)
    Price = models.FloatField(max_length=20,null=False, blank=False)
    Total = models.FloatField(max_length=20, blank=False,null=False)
    Quantity = models.IntegerField(blank=False,null=False)
    Image = models.ImageField(upload_to='cart', blank=False,null=False)
    username = models.CharField(max_length=255, blank=False,null=False)
    cartnumber = models.IntegerField(blank=False,null=False, default=0)
    def __str__(self):
        return self.Product_name
    class Meta:
        ordering = ['Product_name',]    
        


WORK_MODE = (
    ('full','Full Day'),
    ('half', 'Half Day'),
)
class HireModel(models.Model):
    worker_name = models.TextField(max_length=255, blank=False)
    Hire_name = models.TextField(max_length=255, blank=False)
    Name = models.TextField(max_length=255, blank=False)
    Place = models.TextField(max_length=255, blank=False)
    Work_mode = models.CharField(max_length=6, choices=WORK_MODE, default='full')
    Phone = models.BigIntegerField()
    status = models.IntegerField(default=0, blank=False)
    job_title = models.CharField(max_length=20, blank=False,default='none')
    user_status = models.BooleanField(default=False)
    worker_status = models.BooleanField(default=False)
    rating = models.IntegerField(default=0, blank=False)
    # comment = models.CharField(default="",max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class RequestsModel(models.Model):
    hirer = models.TextField(max_length=25, blank=False)
    name = models.TextField(max_length=25, blank=False)
    place = models.TextField(max_length=25, blank=False)
    work_type = models.BooleanField(default=False)
    phone = models.BigIntegerField()
    status =  models.IntegerField(default = 0)
    job_title = models.CharField(max_length=20, blank=False,default='none')
    rate = models.IntegerField(default=500)
    worker_name = models.TextField(max_length=25, blank=False)
    worker_phone = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class CheckoutModel(models.Model):
    product_id = models.IntegerField(blank=True,null=False)
    Products= models.TextField(max_length=100, blank=False,null=False)
    Total = models.FloatField(max_length=20, blank=False,null=False)
    Quantity = models.IntegerField(blank=False,null=False)
    username = models.CharField(max_length=255, blank=False,null=False)
    def __str__(self):
        return self.Product_name        


class PurchaseModel(models.Model):

    phone = models.BigIntegerField(null=True)
    Total = models.FloatField(max_length=20, blank=False,null=False,default=0)

    Prices = ArrayField(models.FloatField(max_length=20, blank=True,null=True))
    Quantity = ArrayField(models.IntegerField(blank=True,null=True))

    Product_name = ArrayField(models.CharField(max_length=100, blank=True,null=True),null=True)

    username = models.CharField(max_length=100, blank=False,null=False)

    first_name = models.TextField(max_length=100, blank=False,null=False)

    last_name = models.TextField(max_length=100, blank=False,null=False)
    
    email = models.TextField(max_length=100, blank=False,null=False)

    street = models.TextField(max_length=100, blank=False,null=False)

    building = models.TextField(max_length=100, blank=False,null=False)

    locality = models.TextField(max_length=100, blank=False,null=False)

    postal = models.IntegerField(blank=False,null=False)

    status =  models.IntegerField(blank=False,null=True,default=1)

    order_id =  models.IntegerField(blank=False,null=False,default=0)

    date = models.DateField()


    def __str__(self):
        return self.username
    class Meta:
        ordering = ['-date',]   
class PackageModel(models.Model):
    package_name = models.CharField(max_length=50,blank=False,null=False)
    validity = models.IntegerField(blank=False,null=False)
    cost = models.FloatField(max_length=20, blank=False,null=False,default=0)
    image = models.ImageField(blank=False,null=False)
class LabopaymentModel(models.Model):
    work_id = models.ForeignKey(RequestsModel, on_delete=models.CASCADE, default=None)
    rate = models.FloatField(max_length=20, blank=False,null=False,default=0)
    status = models.IntegerField(blank=False,null=True,default=0)
    amount = models.FloatField(max_length=20, blank=False,null=False,default=0)