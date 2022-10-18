from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/dashboard.html")

class FundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/fund-management.html")

class TransacView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/transactions.html")

class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/requested-services.html")