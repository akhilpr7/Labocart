from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import datetime
class NewUserModel(AbstractUser):
    phone_no = models.CharField(max_length=16 ,null=True)
    rating = models.IntegerField(null=False, default=0)
    is_sub  = models.BooleanField(default=False)
    wallet  = models.FloatField(default=0.0, blank=False)
    subscribed_at = models.DateField(null=True,blank=True)
    package = models.IntegerField(null=False, default=0)
    image = models.FileField(upload_to='profile/',default="profile/Screenshot_from_2022-08-30_09-59-55.png")
    kyc = models.FileField(upload_to='kyc/',blank=True, null=True)
    kyc_approved  = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username



class labourmodels(models.Model):
    phone = models.BigIntegerField()
    username = models.CharField(max_length=25, blank=False)
    image_link= models.ImageField(upload_to='labour',blank=False)
    job_title = models.CharField(max_length=50, blank=False)
    rate = models.FloatField(max_length=10,default=1)
    work_type = models.BooleanField(default=False)
    status = models.IntegerField(blank = False,default=0)
    job_certificate = models.ImageField(upload_to='credentials',blank=False,null=False,default=0)

    def __str__(self):
        return self.username

class jobmodel(models.Model):
    job_title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255,blank=False)
    

class requests(models.Model):
    username = models.CharField(max_length=255, blank=False)
    worker_username = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=False)

class Wallethistory(models.Model):
    user_id = models.ForeignKey(NewUserModel, on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    date = models.DateField(null=False)
    name =models.CharField(max_length=255, blank=False)
    transactiontype = models.CharField(max_length=255, blank=False)

