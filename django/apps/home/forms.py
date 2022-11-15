from django import forms
from .models import AppliedJobs, Category, JobPostingModel
from authentication.models import NewUserModel,jobmodel

class AddFundForm(forms.Form):
    
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddFundForm, self).__init__(*args, **kwargs)
        self.fields['amount'] = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'1'}))
        print(self.request.user.username)

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
        print(temp)
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
  place = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Place"}))
  image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))
  phone = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Phone"}))
  CHOICES = (('True','Half day'),('False','Full day'))
  work_type = forms.ChoiceField(choices = CHOICES,widget=forms.Select(attrs={'class':'form-select'}))

  def __init__(self,*args,**kwargs):
    self.category = kwargs.pop('initial',[])
    self.user = kwargs.pop('user',[])
    print(self.user,"sdfaghsdhj")
    super(JobPostingForm, self).__init__(*args,**kwargs)
    self.fields['job_title']=forms.ModelChoiceField(queryset=jobmodel.objects.filter(category=self.category).values_list("job_title",flat=True),
                              widget=forms.Select(attrs={'class':'form-select'}))
    self.fields['hirer']=forms.CharField(max_length=20, required=True, widget=forms.HiddenInput() , initial=self.user)

class ApplyForm(forms.ModelForm):
    name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Name",'readonly':'True'}))
    hirer = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Hirer",'readonly':'True'}))
    status = forms.IntegerField(required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Status" ,'readonly':'True'}))
    place = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Place",'readonly':'True'}))
    work_type = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Work type",'readonly':'True'}))
    phone = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Phone number",'readonly':'True'}))
    job_title = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Job title",'readonly':'True'}))
    rate = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Rate", 'label':'rrrrrrrrrrrrrrrrrrrrrr'}))
    worker_name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker name",'readonly':'True' }))
    worker_uname = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker name",'readonly':'True' }))
    worker_phone = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker Phone",'readonly':'True'}))
    class Meta:
        model = AppliedJobs
        fields = '__all__'


class CommentForm( forms.Form ):
    comment = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={'class': 'textarea p-3 rounded-3 w-100 ','placeholder':"Enter your Review",'cols':'200','rows':'5',   }))
    id = forms.CharField(max_length=10, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Worker Phone",'readonly':'True'}))
