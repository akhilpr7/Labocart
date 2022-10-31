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



# Create your views here.


class LoginViews(LoginView):
    template_name = 'accounts/login.html'

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
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
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
            form = RegisterForm(request.POST)
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
        return render(request, self.template)

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.pk
        details = NewUserModel.objects.filter(id=user_id).first()
        context = {"details": details ,'current_path':"Profile" }
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
            updateprofile.image = request.POST['image']
            updateprofile.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm()
        return redirect('update_profile')
