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


class JobPostingModel(models.Model):
    hirer = models.TextField(max_length=255, blank=False)
    name = models.TextField(max_length=255, blank=False)
    place = models.TextField(max_length=255, blank=False)
    work_type = models.BooleanField(default=False)
    phone = models.BigIntegerField()
    status =  models.IntegerField(blank=False,null=True,default=1)
    job_title = models.CharField(max_length=20, blank=False,default='none')
    
