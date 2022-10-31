from django import forms
from .models import Category
from authentication.models import NewUserModel, jobmodel

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