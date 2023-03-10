from django import forms
from .models import AppliedJobs, Category, JobPostingModel,CitiesModel
from authentication.models import NewUserModel,jobmodel

class AddFundForm(forms.Form):
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddFundForm, self).__init__(*args, **kwargs)
        self.fields['amount'] = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'1','max':'9999'}))
        # print(self.request.user.username)

    def clean(self):
        super(AddFundForm,self).clean()
        
        amount = self.cleaned_data.get('amount','')
        
        if amount != '' :
            if float(amount) <= 0:
                 self._errors['amount'] = self.error_class([
                        'Amount cannot be negative.'])
        return self.cleaned_data
    
    def save(self,*args,**kwargs):
        wallet = NewUserModel.objects.filter(username=self.request.user.username).last()
        temp=wallet.wallet +  float(self.cleaned_data['amount'])
        # print(temp)
        wallet.wallet = temp
        wallet.save()

class CategoryForm(forms.Form):
    image=forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))
    category_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Category Name"}))


class AddJobForm(forms.Form):
    job_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Job Name"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all().values_list("category_name",flat=True),widget=forms.Select(attrs={'class':'form-select'}))


class JobPostingForm( forms.Form ):
  name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Name"}))
  place = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Place"}))
#   image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))
  phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Phone",'type':'phone','minlength':'10','maxlength':'10','required pattern':'\d*'}))
  CHOICES = (('True','Full Day'),('False','Half day'))
  work_type = forms.ChoiceField(choices = CHOICES,widget=forms.Select(attrs={'class':'form-select'}))
 
  def __init__(self,*args,**kwargs):
    self.category = kwargs.pop('initial',[])
    # print(self.category,"selllllllllllllllllllllllllffffffffff")
    self.job = kwargs.pop('jobs',[])
    self.user = kwargs.pop('user',[])
    # print(self.user,"sdfaghsdhj")
    super(JobPostingForm, self).__init__(*args,**kwargs)
    self.fields['job_title']=forms.ModelChoiceField(queryset=jobmodel.objects.filter(category=self.category).values_list("job_title",flat=True).exclude(job_title__in=[self.job]),
                              widget=forms.Select(attrs={'class':'form-select'}))
    # print(self.fields['job_title'].__dict__,"joobbbbbb totititititilllleeee")
    self.fields['hirer']=forms.CharField(max_length=20, required=True, widget=forms.HiddenInput() , initial=self.user)

  def clean__job_title(self):
    return self.cleaned_data['job_title']
  def clean(self):

            self.cleaned_data = super().clean()
            place=self.cleaned_data.get('place')
            if place :
                # print("enterd  >>>>>>>>>>>>>>>>>>> 1")
                list=place.split(", ")
                # print("enterd  >>>>>>>>>>>>>>>>>>> list",list )

                if len(list) ==3:
                    # print("enterd  >>>>>>>>>>>>>>>>>>> listhagh;dghd;ghad" )

                    check_place=CitiesModel.objects.filter(name=list[0],subcountry=list[1],country=list[2])
                    # print(check_place)
                    if len(check_place) == 0:
                        self._errors['place']=self.error_class(['Please Select a place from the provided list'])
                        # print("enterd  >>>>>>>>>>>>>>>>>>> 2")
                    else:
                        return self.cleaned_data
                else:
                    self._errors['place']=self.error_class(['Please Select a place from the provided list'])

                    # print("enterd  >>>>>>>>>>>>>>>>>>> 3")

            return self.cleaned_data




class ApplyForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Name",'readonly':'True'}))
    hirer = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Hirer",'readonly':'True'}))
    status = forms.IntegerField(required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Status" ,'readonly':'True'}))
    place = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Place",'readonly':'True'}))
    work_type = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Work type",'readonly':'True'}))
    phone = forms.CharField( required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Phone number",'readonly':'True'}))
    job_title = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Job title",'readonly':'True'}))
    rate = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':"Amount", }))
    worker_name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker name",'readonly':'True' }))
    worker_uname = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker name",'readonly':'True' }))
    worker_phone = forms.CharField( required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker Phone",'readonly':'True'}))
    class Meta:
        model = AppliedJobs
        fields = '__all__'
    def clean(self):

            data = super().clean()
            phone = data['phone'] 
            # print(phone)
            if int(phone) <= 0:

                # print("ssssss")
                self._errors['phone'] = self.error_class([
                    'Phone Number field cannnot be null',])
            elif len(phone)< 6:
                    self._errors['phone'] = self.error_class([
                    'Phone Number should have minimum of 6 letters ',])
            elif len(phone)> 15:
                    self._errors['phone'] = self.error_class([
                    'The length of phone number should be less than 15 ',])

            return self.cleaned_data




class CommentForm( forms.Form ):
    comment = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'textarea p-3 rounded-3 w-100 ','placeholder':"Enter your Review",'cols':'200','rows':'5',   }))
    id = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker Phone",'readonly':'True'}))


# class OTPform(forms.form):
#     otp =forms.CharField(max_length=6,required=True)