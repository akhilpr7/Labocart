from django.shortcuts import render
from django.views import View
# Create your views here.


class LoginViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/login.html")


class RegisterViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, "accounts/register.html")