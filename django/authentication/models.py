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
    image = models.CharField(max_length=3000 ,null=True,default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username



class labourmodels(models.Model):
    username = models.CharField(max_length=25, blank=False)
    image_link= models.CharField(max_length=10000,blank=False)
    job_title = models.CharField(max_length=50, blank=False)
    rate = models.FloatField(max_length=10,default=1)
    work_type = models.BooleanField(default=False)
    status = models.IntegerField(blank = False,default=0)


# class Categorymodel(models.Model):
#     category_name = models.CharField(max_length=30, blank=False)


# class Subcategorymodel(models.Model):
#     job = models.CharField(max_length=50,blank=False)
#     category = models.ForeignKey(Categorymodel, blank=False,on_delete=models.DO_NOTHING)

# class Workersmodel:
#     username = models.ForeignKey(NewUserModel, blank=False,on_delete=models.DO_NOTHING)
#     work_type = models.IntegerField(blank=False)
#     rate = models.FloatField(max_length=10,default = 1)
class jobmodel(models.Model):
    job_title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255,blank=False)
    

class requests(models.Model):
    username = models.CharField(max_length=255, blank=False)
    worker_username = models.CharField(max_length=255, blank=False)
    #status codes
    #true = active(worker able to see the request)
    #false = inactive(the request is not active)
    status = models.BooleanField(default=False)
