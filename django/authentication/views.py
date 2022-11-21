from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm,UpdateProfileForm
from .models import NewUserModel
from ecommerce.models import HireModel
from django.db.models import Q
from django.conf import settings  
from django.views.decorators.cache import cache_control
from apps.home.models import Category
from django.utils.safestring import mark_safe
import json
from json import dumps





# Create your views here.


class LoginViews(LoginView):
    template_name = 'accounts/login.html'
    # print(settings.NEW_VAR)
    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = LoginForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST['username'])
        print(request.POST['password'])
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.kyc_approved:
                login(request, user)
                if request.user.is_superuser:
                    return HttpResponseRedirect(reverse('admindashboard'))
                else:
                    return HttpResponseRedirect(reverse('dashboard'))
            else:
                messages.error(request, "Your KYC details haven't been approved yet!. Please try again later.")
                return redirect(reverse('login'))
        else:
            messages.error(request, 'Incorrect username or password')
            return redirect(reverse('login'))


class RegisterViews(View):
    template = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = RegisterForm()
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST,request.FILES)
            print(request.POST['username'])
            if form.is_valid():
                print("valid")

                try:
                    form.save()
                except Exception as e:
                    print("error", e)
                    return render(request, 'accounts/register.html', {'form': RegisterForm(request.POST)})

                messages.success(
                    request, 'Your account has been created ! You are now able to log in')
                return redirect(reverse('login'))
            else:
                print("not valid")
                messages.error(request, 'Registration failed')
                return render(request, 'accounts/register.html', {'form': form})

        return render(request, self.template, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class Demo(View):
    template = 'home/tables-bootstrap-tables.html'
    
    def get(self, request, *args, **kwargs):
        from django.http import HttpResponse
        return HttpResponse("helo2")
        data = Category.objects.all()
        context={
            'data':data,
    		'MEDIA_ROOT':settings.NEW_VAR,

        }
        return render(request, self.template,context)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.pk
        details = NewUserModel.objects.filter(id=user_id).first()
        data = list(HireModel.objects.filter(Q(worker_name=request.user)&Q(status=4)&~Q(comment="")).values())
        userimage = NewUserModel.objects.all().values()
        print(data)
        context = {
            "details": details ,
            'current_path':"Profile",
            'comments' : data,
            "user" :userimage

             }
        return render(request, 'accounts/profile.html',context)



class UpdateProfileView(View):
    def get(self,request, *args, **kwargs):
        user = NewUserModel.objects.get(id=request.user.id)
        data = {
            "first_name": user.first_name,
			"last_name": user.last_name,
			"phone_no": user.phone_no,
			"email": user.email,
            "image": user.image,
        }
        context ={'current_path':"Update Profile" }
        form = UpdateProfileForm(data)
        context['form'] = form
        return render(request, 'home/update_profile_form.html',context)

    def post(self, request, *args, **kwargs):
        id = request.user.id
        if request.method == 'POST':
            updateprofile = NewUserModel.objects.get(id=id)
            updateprofile.first_name = request.POST['first_name']
            updateprofile.last_name = request.POST['last_name']
            updateprofile.phone_no = request.POST['phone_no']
            updateprofile.email = request.POST['email']
            updateprofile.image = request.FILES['image']
            updateprofile.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm()
        return redirect('update_profile')

