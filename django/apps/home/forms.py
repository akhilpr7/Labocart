from django import forms
from .models import Category, JobPostingModel
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

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Category Name"}))
    class Meta:
        model = Category
        fields = '__all__'

class AddJobForm(forms.Form):
    job_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Job Name"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all().values_list("category_name",flat=True))


class JobPostingForm( forms.ModelForm ):
  name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Name"}))
  place = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Place"}))
  phone = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Your Phone"}))
  work_mode = forms.CharField(max_length=5, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
#   worker_name = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"worker name ", 'readonly':'readonly'}))
  hirer = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Hire name", 'readonly':'readonly'}))
  job_title = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput(attrs={'class': 'form-control','placeholder':"Job title", 'readonly':'readonly'}))
  rate = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control border ps-2','min':'1'}))


  class Meta:
    model = JobPostingModel
    fields = ('name','place','phone','work_mode', 'hirer','job_title','rate')    
  def __init__(self,*args,**kwargs):
    print(kwargs,"88888888888888888888888888")
    self.category = kwargs.pop('initial',[])
    print(kwargs,"88888888888888888888888888",self.category)
    super(JobPostingForm, self).__init__(*args,**kwargs)
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