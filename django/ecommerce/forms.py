import abc
from dataclasses import field
from pyexpat import model
from random import choices
from unicodedata import category
from urllib import request
from django import forms
from django.forms import ModelForm
from .models import ProductsModel,HireModel,CartModel,PurchaseModel,PackageModel
from authentication.models import jobmodel
from django.core.validators import validate_email

class AddStockForm( forms.ModelForm ):

  Product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  Price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  Quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2' ,'min':'1'}))
  Image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  class Meta:
    model = ProductsModel
    fields = ('Product_name','Price','Quantity','Image',)
  
class Laboregisterform(forms.Form):


  def __init__(self,*args,**kwargs):
    print(kwargs,"88888888888888888888888888")
    self.category = kwargs.pop('initial',[])
    print(kwargs,"88888888888888888888888888",self.category)
    super(Laboregisterform, self).__init__(*args,**kwargs)
    # choice =jobmodel.objects.filter(category=self.category).values_list("job_title",flat=True)
    self.fields['job_title']=forms.ModelChoiceField(queryset=jobmodel.objects.filter(category=self.category).values_list("job_title",flat=True))
  #   category = self.category
  #   return category
  # def __init__(self, *args, **kwargs) :
    # print("hhhhhhhhhhh",self.__dict__)
    # self.category = kwargs.pop("category",None)
    # print("dfdfdgdgdgdgd",kwargs)

    # datas =list(jobmodel.objects.filter(category=self.category).values_list('job_title'))
    # choices = datas
    # for data in datas:
    #   print(data,"gggggggggggggggggggggggggggggggggggg",)
  #   # self.fields['job_title'] = forms.ChoiceField(choices=choices) 
  #   # job_title = forms.ChoiceField(choices=choices) 
  #   super(Laboregisterform, self).__init__(*args, **kwargs)
  #   # self.fields['job_title'] = forms.ChoiceField(data) 

  # username = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control border ps-2'}))
    print(self.category,"-----------------------------------------")
    cat = self.category
  # category1 = self.category
  image_link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  # job_title = forms.ModelChoiceField(queryset=jobmodel.objects.filter(category=self.category).values_list("job_title"))
  # job_title = forms.ModelChoiceField(queryset=jobmodel.objects.filter(category=cat).values_list("job_title"))
  rate = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  CHOICES = (('True','Half day'),('False','Full day'))
  work_type = forms.ChoiceField(choices = CHOICES)

  # class Meta:
  #   model = labourmodels
  #   fields = ('username','image_link','job_title','rate','work_type',)

class AddToCartForm( forms.ModelForm ):

  Product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  Price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  Quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  Image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  cartnumber = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  class Meta:
    model = CartModel
    fields = '__all__'

class UpdateStockForm( forms.ModelForm ):
  id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly':'true','maxlength':'10'}))
  Product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  Price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  Quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  Image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  class Meta():
    model = ProductsModel
    fields = '__all__'

class PurchaseForm(forms.Form):
  
  phone = forms.CharField(max_length = 10 , widget=forms.NumberInput(attrs={"placeholder": "Phone",'class': 'form-control','minlength':'10','maxlength':'10'}))
  
  first_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Firstname",'class': 'form-control','minlength':'3'}))

  last_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Lastname",'class': 'form-control','minlength':'3','min':'0'}))

  email = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Email",'type':'email', 'class': 'form-control'}))

  street = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Street",'class': 'form-control','minlength':'3'}))

  building = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Building/House No",'class': 'form-control','minlength':'3'}))

  locality = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Locality",'class': 'form-control','minlength':'3'}))

  postal = forms.IntegerField( widget=forms.NumberInput(attrs={"placeholder": "Zip code",'class': 'form-control', 'max':'999999 '}))

  
  def clean(self):

            data = super().clean()

            print(data)
            print("Data",data['phone'])
            phone = data['phone'] 
            email = data['email']
            if validate_email(email) :
                print("ssssss")

                self._errors['email'] = self.error_class([
                    'Enter a valid email address',])
            if int(phone) <= 0:
                print("ssssss")
                self._errors['phone'] = self.error_class([
                    'Phone Number field cannnot be null',])
      
            return self.cleaned_data








class HireNowForm( forms.ModelForm ):
  Name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Name"}))
  Place = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Place"}))
  Phone = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Phone"}))
  # Work_mode = forms.CharField(max_length=5, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
  worker_name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"worker name ", 'readonly':'readonly'}))
  Hire_name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Hire name", 'readonly':'readonly'}))
  job_title = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Job title", 'readonly':'readonly'}))
  

  class Meta:
    model = HireModel
    fields = ('Name','Place','Phone','Work_mode', 'Hire_name','worker_name','job_title')

class CheckoutForm(forms.Form):
  Quantity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ','style':'width:50px;','min':'1'}))
  total = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ','style':'width:100px;','min':'1'}))





class UpdatePackageForm( forms.ModelForm ):
  id = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly':'true','maxlength':'10'}))
  package_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  validity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  cost = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  class Meta():
    model = PackageModel
    fields = '__all__'



class AddPackageForm( forms.ModelForm ):

  package_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  validity = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  cost = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))
  image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border ps-2'}))
  class Meta:
    model = PackageModel
    fields = ('package_name','validity','cost','image',)