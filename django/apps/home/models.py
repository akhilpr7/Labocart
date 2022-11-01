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

WORK_MODE = (
    ('full','Full Day'),
    ('half', 'Half Day'),
)
class JobPostingModel(models.Model):
    hirer = models.TextField(max_length=255, blank=False)
    name = models.TextField(max_length=255, blank=False)
    place = models.TextField(max_length=255, blank=False)
    work_mode = models.CharField(max_length=6, choices=WORK_MODE, default='full')
    phone = models.BigIntegerField()
    status = models.IntegerField(default=0, blank=False)
    job_title = models.CharField(max_length=20, blank=False,default='none')
    rate = models.FloatField(max_length=10,default=1)
