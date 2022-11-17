from email.mime import image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUserModel
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):

    phone_no = forms.CharField(max_length = 10 , widget=forms.NumberInput(attrs={"placeholder": "Phone",'class': 'form-control','minlength':'10','maxlength':'10'}))

    username = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Username",'class': 'form-control','minlength':'3'}))
    first_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Firstname",'class': 'form-control','minlength':'3'}))
    # wallet = forms.CharField(max_length = 30 , widget=forms.NumberInput(attrs={"placeholder": "Amount",'class': 'form-control','min':'1'}))
    last_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Lastname",'class': 'form-control','minlength':'3','min':'0'}))
    email = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Email",'type':'email', 'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, widget = forms.PasswordInput(attrs={"placeholder": "Password",'class': 'form-control','minlength':'8'}))
    password2 = forms.CharField(max_length=30, widget = forms.PasswordInput(attrs={"placeholder": "Password check",'class': 'form-control','minlength':'8','pattern':'[A-Za-z0-9@._-$]' }))
    image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))
    kyc = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):

        model = NewUserModel

        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','phone_no','kyc','image' )

    def clean(self):

            data = super().clean()

            print(data)
            print("===========data",data['phone_no'])
            phone = data['phone_no'] 
            if int(phone) <= 0:
                print("ssssss")
                self._errors['phone_no'] = self.error_class([
                    'Phone Number field cannnot be null',])
      
            return self.cleaned_data



class LoginForm(forms.Form):
 
    username = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Username"}))
    password = forms.CharField(max_length=15, widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':"Password"}))



class UpdateProfileForm(UserCreationForm):

    phone_no = forms.CharField(max_length = 10 , widget=forms.NumberInput(attrs={"placeholder": "Phone",'class': 'form-control','minlength':'10','maxlength':'10'}))
    first_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Firstname",'class': 'form-control','minlength':'3'}))
    last_name = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Lastname",'class': 'form-control','minlength':'3','min':'0'}))
    email = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={"placeholder": "Email",'type':'email', 'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):

        model = NewUserModel
        fields = ('first_name','last_name','phone_no','email','image',)
