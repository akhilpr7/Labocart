from django.shortcuts import render
from django.views import View
# Create your views here.
class Home(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html',{})
class Shop(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'shop.html',{})
class LaboShop(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'labo-shop.html',{})
