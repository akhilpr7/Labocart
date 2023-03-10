from calendar import c
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, null=False)
    image = models.FileField(upload_to='categoryImages/')

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
    is_active = models.BooleanField(default=True)
    phone = models.BigIntegerField()
    status =  models.IntegerField(blank=False,null=True,default=0)
    job_title = models.CharField(max_length=20, blank=True,default='none')

    class Meta:
        ordering = ['id']

class AppliedJobs(models.Model):
    hirer = models.TextField(max_length=25, blank=False)
    name = models.TextField(max_length=25, blank=False)
    place = models.TextField(max_length=255, blank=False)
    work_type = models.BooleanField(default=False)
    phone = models.BigIntegerField()
    status =  models.IntegerField(default = 0)
    job_title = models.CharField(max_length=20, blank=False,default='none')
    rate = models.IntegerField(default=500)
    worker_name = models.TextField(max_length=25, blank=False)
    worker_uname = models.TextField(max_length=25, blank=False)
    worker_phone = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    copy_status = models.BooleanField(default=False)
    work_date = models.DateTimeField(auto_now_add=True)

class JobPaymentModel(models.Model):
    work_id = models.ForeignKey(AppliedJobs, on_delete=models.CASCADE, default=None)
    rate = models.FloatField(max_length=20, blank=False,null=False,default=0)
    status = models.IntegerField(blank=False,null=True,default=0)
    amount = models.FloatField(max_length=20, blank=False,null=False,default=0)




class CitiesModel(models.Model):

    name=models.CharField(max_length=100,null=True,blank=False)

    country=models.CharField(max_length=100,null=True,blank=False)

    subcountry=models.CharField(max_length=100,null=True,blank=False)

    geonameid=models.IntegerField(default=1,null=True,blank=False)    

class ReeportModel(models.Model):
    username=models.CharField(max_length=100,null=False,blank=False)
    woh=models.BooleanField(null=False,blank=False)
    hireid=models.IntegerField(null=False,blank=False)
    email=models.CharField(max_length=30,null=False,blank=False)
    phone=models.CharField(max_length=10, blank=False,null=False)
    issue=models.CharField(max_length=255, blank=False,null=False)
    proof=models.ImageField(upload_to='issues',blank=False)
