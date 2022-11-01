from django.contrib import messages
from authentication.models import NewUserModel, jobmodel
from django.shortcuts import render, redirect
from django.views import View
from authentication.models import NewUserModel, labourmodels
from django.db.models import Q
from django.urls import reverse
from ecommerce.models import HireModel, ProductsModel, CartModel
from .forms import AddStockForm, HireNowForm,Laboregisterform,PurchaseForm,AddPackageForm
from apps.home.models import Category
from .forms import UpdateStockForm,CheckoutForm,UpdatePackageForm
from .models import HireModel, PackageModel, PurchaseModel
import datetime
from datetime import date, datetime
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import random,datetime

@method_decorator(login_required,name='dispatch')
class Home(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html', {})


@method_decorator(login_required,name='dispatch')
class Shop(View):
	def get(self, request, *args, **kwargs):
		print("aaaaaaaaaaaaaaaaaaaa",request)
		print("bbbbbbbbbbbbbbbbbbbbbbb",request.GET.get('orderby'))
		if request.GET.get('orderby') is not None and request.GET.get('orderby') != '':
			if request.GET.get('orderby') == 'atoz':
				product = ProductsModel.objects.all().order_by("Product_name")
			elif request.GET.get('orderby') == 'ztoa':
				product = ProductsModel.objects.all().order_by("-Product_name")
			elif request.GET.get('orderby') == 'latest':
				product = ProductsModel.objects.all().order_by("id")
			elif request.GET.get('orderby') == 'oldest':
				product = ProductsModel.objects.all().order_by("-id")
		else:
			product = ProductsModel.objects.all()
		cart = CartModel.objects.all().filter(username=request.user.username).values_list("Product_name",flat=True)
		data = {
		"product":product,
		'form':PurchaseForm(),
		'current_path':"Shop",
		'cart' : cart,

		}

		return render(request, 'shop.html', data)
		

@method_decorator(login_required,name='dispatch')
class CartView(View):
	template = 'cart.html'
	

	def get(self, request, *args, **kwargs):
		products = list(CartModel.objects.filter(username=request.user.username).values())
		totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))
		context = {
		"products":products,
		'form':CheckoutForm(),
		'current_path':"Cart" ,
		'totalPrice': totalPrice["Total__sum"],
		}	
		return render(request, self.template, context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			return redirect('checkout')

		else:   
			return redirect('cart')
			

@method_decorator(login_required,name='dispatch')
class AddtocartView(View):

	def get(self, request, id, *args, **kwargs):
		product = list(ProductsModel.objects.filter(id=id).values())[0]
		print("The product is:", product)
		print(product["id"])
		data = CartModel(
			username=request.user.username,
			Total=product["Price"],
			Price=product["Price"],
			Product_name=product["Product_name"],
			Quantity=1,
			Image=product["Image"],
			product_id=product["id"],
			cartnumber = request.user.id,
		)
		messages.success(request,"Success !")
		data.save()
		return redirect('shop')
@method_decorator(login_required,name='dispatch')
class IncreaseNo(View):
	def get(self, request, id, *args, **kwargs):
		price = CartModel.objects.filter(product_id=id,username= request.user.username).values_list('Price')[0][0]
		quantity = CartModel.objects.filter(product_id=id,username= request.user.username).values_list('Quantity')[0][0]
		total = (quantity + 1 ) * price
		print("toal product price",quantity)
		print("toal product price",int(price))
		print("toal product price",total)
		CartModel.objects.filter(product_id=id,username= request.user.username).update(Quantity = quantity + 1 ,  Total= total)
		return redirect('cart')

@method_decorator(login_required,name='dispatch')
class DecreaseNo(View):
	def get(self, request, id, *args, **kwargs):
		price = CartModel.objects.filter(product_id=id,username= request.user.username).values_list('Price')[0][0]
		quantity = CartModel.objects.filter(product_id=id,username= request.user.username).values_list('Quantity')[0][0]
		total = (quantity - 1 ) * price
		print("toal product price",quantity)
		print("toal product price",price)
		print("toal product price",total)

		if quantity <= 1:
			messages.error(request,"Error !")
			return redirect('cart')
		else:
			CartModel.objects.filter(product_id=id,username= request.user.username).update(Quantity = quantity - 1, Total = total )
			return redirect('cart')
		

@method_decorator(login_required,name='dispatch')
class DelFromCartView(View):
	def get(self, request, id):
		cartData = CartModel.objects.filter(product_id=id)
		cartData.delete()
		messages.success(request,"Successfully deleted !")
		return redirect('cart')



@method_decorator(login_required,name='dispatch')
class CheckoutView(View):
	
	template = 'checkout.html'

	def get(self, request, *args, **kwargs):
		products = list(CartModel.objects.filter(username=request.user.username).values())
		totalPrice = CartModel.objects.aggregate(Sum('Total'))
		# items = list(PurchaseModel.objects.filter(username=request.user.username,status = 1).values_list('Prices',flat=True))[0]
		# print(items)
		context = {
		"products":products,
		'form':PurchaseForm(),
		'current_path':"Checkout" ,
		'totalPrice': totalPrice["Total__sum"],
		}	
		return render(request, self.template, context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = PurchaseForm(request.POST)
			if form.is_valid():
					
					Prices = list(CartModel.objects.filter(username=request.user.username).values_list('Total',flat=True))
					Quantity = list(CartModel.objects.filter(username=request.user.username).values_list('Quantity',flat=True))
					n = random.randint(0,99999)
			
					# request.session['Prices']= Prices_invoice
					# request.session['Quantity']= Quantity_invoice
					# request.session['Names']= Names_invoice
					request.session['order']= n
					request.session['Building']= request.POST['building']
					request.session['Street']= request.POST['street']
					request.session['Locality']= request.POST['locality']

					product_name = list(CartModel.objects.filter(username=request.user.username).values_list('Product_name',flat=True))
					totalPrice = CartModel.objects.aggregate(Sum('Total'))
					data = PurchaseModel(	
						phone=request.POST['phone'],
						Total=totalPrice["Total__sum"],
						Prices=Prices,
						Quantity=Quantity,
						Product_name=product_name,
						username=request.user.username,
						first_name=request.POST['first_name'],
						last_name=request.POST['last_name'],
						email=request.POST['email'],
						street=request.POST['street'],
						building=request.POST['building'],
						locality=request.POST['locality'],
						postal=request.POST['postal'],
						order_id=n,
						date = datetime.datetime.now().date()
					)
					data.save()
					id = PurchaseModel.objects.filter(order_id=n).values_list("id")[0][0]

					print("valid")
					print("iiiiiiiiiiiiddddddddddd",id)
					return redirect('payment',id)
			return render(request,self.template, {'form': PurchaseForm(request.POST)})

		else:   
			return redirect('shop')
			

class Invoice(View):
	template_name = 'invoice.html'
	def get(self, request):
		products = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Product_name')[0]
		print(products, "Prodduuuuuucts")
		prices = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Prices')[0]
		quantity = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Quantity')[0]
		print(prices, "priceeeeeeeeeeeeeeeees")
		total = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Total')[0][0]
		print(total, "total")

		context = {

		"total": total,

		"products": products,

		"prices": prices,

		"quantity": quantity,
		}
		return render(request, self.template_name, context)



@method_decorator(login_required,name='dispatch')
class LaboShop(View):
	def get(self, request, *args, **kwargs):
		data = labourmodels.objects.filter(Q(status=1) | Q(status=2) | Q(status=3))
		fund = NewUserModel.objects.filter(username=request.user.username).values('wallet')
		print("fffffffffffffffffffffffffffffffffffffffffffffff",fund)
		context = {
			'data': data,
			'current_path':"Request services",
			'fund': fund
		}
		is_sub = NewUserModel.objects.filter(username=request.user.username).values_list('is_sub')[0][0]
		# print(is_sub,"sdddddddddddddddddddd")
		if is_sub:
			return render(request, 'labo-shop.html', context)
		else:
			messages.error(request,"Membership Required !")
			return redirect("membership")


@method_decorator(login_required,name='dispatch')
class Addproduct(View):
	template = 'addStock.html'
	def get(self, request, *args, **kwargs):
		form = AddStockForm
		context = { 
					'form': form,
					'data': 'Add Stock',
					'current_path':"Add Stock", 
				  }
   
		return render(request,self.template,context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = AddStockForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request,"Successfully Added !")
				return redirect('stocklist')
			else:
				return redirect('addproduct')
							# print(form.cleaned_data.get('nothing'))
		else:   
			form = AddStockForm()
			return render(request, self.template)

@method_decorator(login_required,name='dispatch')
class Deleteproduct(View):
	def get(self, request, id):
		productData = ProductsModel.objects.get(id=id)
		productData.delete()
		messages.succes(request,"Success !")
		return redirect('stocklist')
@method_decorator(login_required,name='dispatch')
class UpdateProduct(View): 
	def get(self, request,id, *args, **kwargs):
			productData = ProductsModel.objects.get(id=id)
			data = {"id": productData.id,
			"Product_name": productData.Product_name,
			"Price" : productData.Price,
			"Quantity" : productData.Quantity,
			"Image" : productData.Image,              
			}
			context ={'current_path':"Update Stock" }
			form    = UpdateStockForm(data)
			context['form'] = form
			return render(request, 'updatestock.html', context)
	
	def post(self, request, *args, **kwargs):
		id = request.POST['id']
		if request.method == 'POST':

			updatedRecord = ProductsModel.objects.get(id=id)

			updatedRecord. Product_name = request.POST['Product_name']
			updatedRecord. Price = request.POST['Price']
			updatedRecord. Quantity = request.POST['Quantity']
			updatedRecord. Image = request.POST['Image']
			updatedRecord.save()
			messages.success(request,"Success!")
			return redirect('stocklist')
		else:
			form = UpdateStockForm()
		return redirect(request, 'updatestock')

@method_decorator(login_required,name='dispatch')
class ProductTable(View):
	template = 'stocktable.html'
	def get(self, request, *args, **kwargs):
		products = ProductsModel.objects.all().order_by('id')
		context = {
			'prod' : products,
			'current_path':"Stock Table" 
		}
		return render(request, self.template, context=context)


@method_decorator(login_required,name='dispatch')
class LaboRegister(View):
	template = 'laboregister.html'
	def get(self, request,id, *args, **kwargs):
		category = Category.objects.filter(id=id).values_list('category_name')[0][0]
		jobs = jobmodel.objects.filter(category=category).values()
		# print("----",jobs,"6666666666666666666666666666666")
		form = Laboregisterform(initial=category)
		context = {
			"form" : form,
			"jobs" : jobs,
			'current_path':"Apply Services" 
		}
		# if not request.user.is_superuser:
		return render(request, self.template,context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = Laboregisterform(request.POST)
			print(request.POST.get("image_link"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("job_title"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("rate"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("work_type"),"image linkkkkkkkkkkkkkk")
			print(form.errors,"errrrororororororoor")
			# labourmodels['username']=request.user.username
			job_title = request.POST.get('job_title')

			form.fields['job_title'].choices = [(job_title, job_title)]
			# if form.is_valid():
				# print(form.cleaned_data,"ffffffffffffffffffffffffffff")
			image_link = request.POST.get("image_link")
			job_title = request.POST.get("job_title")
			rate = request.POST.get("rate")
			work_type = request.POST.get("work_type")
			
			obj = labourmodels.objects.create(username=request.user,image_link=image_link,job_title=job_title,rate=rate,work_type=work_type,status = 1)
				# usename = request.user.username,
				# image_link = form.cleaned_data["image_link"],
				# job_title = form.cleaned_data["job_title"],
				# rate = form.cleaned_data["rate"],
				# work_type = form.cleaned_data["work_type"]
			# form.save()
			messages.success(request,"Success !")
			print(obj,"55555555555555")
			return redirect('shop')
			# else:
			# 	print(form.errors)    
			# 	return render(request, self.template, {'form': form})

@method_decorator(login_required,name='dispatch')
class Checkout(View):
	template = 'checkout.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template, {})


@method_decorator(login_required,name='dispatch')
class Labocategories(View):
	template = 'labo_categories.html'
	def get(self, request, *args, **kwargs):
		data = Category.objects.all()
		context = {	
			"data" : data,
			'current_path':"Apply Services" 
		}
		total_work = labourmodels.objects.filter(Q(username=request.user.username)&((Q(status=1)|Q(status=2)|Q(status=3)))).count()
		print(total_work,"totttttttttttttttttttaaaaaaal workkkkkkkkkkkkk")
		if total_work < 5 :
			return render(request, self.template,context)
		else:
			messages.error(request,"Job Applying Limit Reached !!")
			return redirect("laboshop")


@method_decorator(login_required,name='dispatch')
class ActiveServices(View):
	def get(self, request, *args, **kwargs):
		data = labourmodels.objects.filter(Q(username = self.request.user.username) & (Q(status=0) | Q(status=1) | Q(status=2)))
		context = {
			"data" : data,
			'current_path':"ActiveServices"
		}
		return render(request,'activeServices.html',context)

@method_decorator(login_required,name='dispatch')
class HireNowView(View):
	def get(self, request, *args, **kwargs):
		username = kwargs.get('username')
		job_title = kwargs.get('job_title')
		data = {
			"worker_name" :username,
			"Hire_name" : request.user,
			"job_title" : job_title
		}
		form = HireNowForm(data)
        # print("eeeeeeeeeeeeeeeeeeeeeeeeee",username)
		context = {'form': form}
		return render(request, "hireNowForm.html",context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = HireNowForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request,'Your request Succesfully created')
				return redirect('requested')
			else:
				messages.error(request,'Unsuccesfull')
				return redirect('dashboard')
@method_decorator(login_required,name='dispatch')
class CancelRequest(View):
	def get(self, request,id):
		requests = HireModel.objects.get(id=id)
		requests.delete()
		messages.success(request,"Success !")
		return redirect('requested')
@method_decorator(login_required,name='dispatch')
class Assignedworks(View):
	def get(self, request, *args, **kwargs):
		template = 'assigned_works.html'
		services = HireModel.objects.filter(Q(worker_name = request.user.username) &( Q(status=0)| Q(status=1)))
		print(services,"--------------------------------------------")
		context = {
			"data": services,
			'current_path':"Assigned Services"
		}
		return render(request,template,context)
@method_decorator(login_required,name='dispatch')
class Acceptservice(View):
	def get(self,request,id, *args, **kwargs):
		# serviceobj = HireModel.objects.get(id=id)
		status = HireModel.objects.filter(id=id).values_list("status")[0][0]
		print(status,"----sbsjdsdsldsldshdshldhsdh-----") 
		if status == 0:
			HireModel.objects.filter(id=id).update(status=3)
			return redirect('assigned')
		elif status ==1:
			return redirect('laboshop')
		else:
			return redirect('labocategory')
@method_decorator(login_required,name='dispatch')	
class Togglestatus(View):
	def get(self, request,id, *args, **kwargs):
		status = labourmodels.objects.filter(id=id).values_list("status")[0][0]
		print(status,":::::::::::::::::::::::")
		if status == 0:
			total_work = labourmodels.objects.filter(Q(username=request.user.username)&((Q(status=1)|Q(status=2)|Q(status=3)))).count()
			if total_work <5:
				labourmodels.objects.filter(id=id).update(status=1)
				messages.success(request,"Success !")
				return redirect("active_service")
			else:
				messages.error(request,"Maximum Job Limit Reached !!!")
				return redirect("active_service")
		elif status ==1:
			labourmodels.objects.filter(id=id).update(status=0)
			messages.success(request,"Success !")
			return redirect("active_service")
		elif status ==2:
			labourmodels.objects.filter(id=id).update(status=0)
			messages.success(request,"Success !")
			return redirect("active_service")
		else:
			return redirect("active_service")
@method_decorator(login_required,name='dispatch')
class Subscribe(View):
	def get(self, request,id, *args, **kwargs):
		is_sub = NewUserModel.objects.filter(username=request.user.username).values_list("is_sub")[0][0]
		wallet_balance = NewUserModel.objects.filter(username=request.user.username).values_list("wallet")[0][0]
		print(is_sub,"***************************")
		print(wallet_balance,"***************************")
		packagecost = PackageModel.objects.filter(id=id).values_list("cost")[0][0]
		packagename = PackageModel.objects.filter(id=id).values_list("package_name")[0][0]
		print(packagecost,"packageeeeee coostssss")
		if wallet_balance>= packagecost:
			if is_sub:
				messages.error(request,"Already Subscribed")
				return redirect ("laboshop")
			elif is_sub == False:

				n = random.randint(0,99999)
				data = PurchaseModel(	
					phone=request.user.phone_no,
					Total=packagecost,
					Prices=[packagecost],
					Quantity=[1],
					Product_name=[packagename],
					username=request.user.username,
					first_name=request.user.first_name,
					last_name=request.user.last_name,
					email=request.user.email,
					street="",
					building="",
					locality="",
					postal=676122,
					order_id=n,
					status=0,
					date = datetime.datetime.now().date()
				)
				data.save()
				NewUserModel.objects.filter(username=request.user.username).update(is_sub=True,wallet=wallet_balance-packagecost,subscribed_at=datetime.datetime.now().date(),package=id)	
				messages.success(request,"Succesfully Subscribed")
				return redirect ("laboshop")
			else:
				messages.error(request,"Error")
				return redirect ("laboshop")
		else:
			messages.error(request,"Not enough balance in wallet!")
			return redirect ("laboshop")
		
class HomePage(View):
	def get(self, request, *args, **kwargs):
		template = 'Homepage/Homepage.html'
		return render(request,template,{})
class Payment(View):
	def get(self, request, id, *args, **kwargs):
		template= 'payment.html'
		products= PurchaseModel.objects.filter(id=id).values_list('Product_name')[0]
		# print(products,"Prodduuuuuucts") 
		prices = PurchaseModel.objects.filter(id=id).values_list('Prices')[0]
		quantity = PurchaseModel.objects.filter(id=id).values_list('Quantity')[0]
		# print(prices,"priceeeeeeeeeeeeeeeees")
		total= PurchaseModel.objects.filter(id=id).values_list('Total')[0][0]
		print(total,"total")

		context={
			"total":total,
			"products":products,
			"prices":prices,
			"id":id,
			"quantity":quantity,

		}
		return render(request,template,context)

class ConfirmPay(View):
	def get(self, request,id, *args, **kwargs):
		wallet_balance = NewUserModel.objects.filter(username=request.user.username).values_list("wallet")[0][0]
		total_price=PurchaseModel.objects.filter(id=id).values_list("Total")[0][0]
		if wallet_balance >= total_price:
			NewUserModel.objects.filter(username=request.user.username).update(wallet=wallet_balance-total_price)
			PurchaseModel.objects.filter(id=id).update(status=3)
			messages.success(request,"Payment Successful")
			obj = CartModel.objects.filter(username=request.user.username)
			# products = PurchaseModel.objects.filter(id=id).values_list("Product_name")[0]
			# quantity = PurchaseModel.objects.filter(id=id).values_list("Quantity")[0]
			product_id = CartModel.objects.filter(username=request.user.username).values_list("product_id")
			
			for i in product_id:
				print(i[0],"hhhhhhhhhhhhhhhhhhhhhh")
				quantity = CartModel.objects.filter(product_id=i[0]).values_list("Quantity")[0][0]
				print(quantity,"quannnnnnntititititi")
				quant = ProductsModel.objects.filter(id=i[0]).values_list("Quantity")[0][0]
				ProductsModel.objects.filter(id=i[0]).update(Quantity=quant-quantity)
			obj.delete()
			return redirect("invoice")
		else:
			messages.error(request,"Not enough balance in wallet!!")
			PurchaseModel.objects.filter(id=id).update(status=2)
			return redirect("payment",id)

class Packages(View):
	def get(self, request, *args, **kwargs):
		template = 'packages.html'
		package = PackageModel.objects.all()
		context = {
			"package":package,

		}
		return render(request,template,context)


@method_decorator(login_required,name='dispatch')
class Deletepackage(View):
	def get(self, request, id):
		packageData = PackageModel.objects.get(id=id)
		packageData.delete()
		messages.success(request,"Success !")
		return redirect('packages')

@method_decorator(login_required,name='dispatch')
class UpdatePackage(View): 
	def get(self, request,id, *args, **kwargs):
			packageData = PackageModel.objects.get(id=id)
			data = {
			"id":packageData.id,
			"Package_name": packageData.package_name,
			"Validity" : packageData.validity,
			"Cost" : packageData.cost,
			"Image" : packageData.image,              
			}
			context ={'current_path':"Update Package" }
			form    = UpdatePackageForm(data)
			context['form'] = form
			return render(request, 'updatepackage.html', context)
	
	def post(self, request, *args, **kwargs):
		id = request.POST['id']
		if request.method == 'POST':

			updatedRecord = PackageModel.objects.get(id=id)

			updatedRecord. package_name = request.POST['package_name']
			updatedRecord. validity = request.POST['validity']
			updatedRecord. cost = request.POST['cost']
			updatedRecord. image = request.POST['image']
			updatedRecord.save()
			messages.success(request,"Success!")
			return redirect('packages')
		else:
			form = UpdatePackageForm()
		return redirect(request, 'updatepackage')


@method_decorator(login_required,name='dispatch')
class Addpackage(View):
	template = 'addpackage.html'
	def get(self, request, *args, **kwargs):
		form = AddPackageForm
		context = { 
					'form': form,
					'data': 'Add Package',
					'current_path':"Add Package", 
				  }
   
		return render(request,self.template,context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = AddPackageForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request,"Successfully Added !")
				return redirect('packages')
			else:
				return redirect('addpackage')
							# print(form.cleaned_data.get('nothing'))
		else:   
			form = AddPackageForm()
			return render(request, self.template)

class membership(View):
	def get(self, request, *args, **kwargs):
		template = "membership_card.html"
		data = PackageModel.objects.all()
		context={
			"data": data,
		}
		return render(request,template,context)
class Workerview(View):
	def get(self, request, *args, **kwargs):
		return render(request,'index1.html',{})