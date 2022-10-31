from calendar import c
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, null=False)

class Transaction(models.Model):
    username = models.CharField(max_length=255, null=False)
    product_name = models.CharField(max_length=255, null=False)
    total_price = models.IntegerField(blank=False , null=False)
    date = models.DateField(null=False)
    quantity = models.IntegerField(blank=False,null=False)
    Status = models.CharField(max_length=100, null=False)



