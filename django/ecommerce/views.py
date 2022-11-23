from django.contrib import messages
from authentication.models import NewUserModel, jobmodel
from django.shortcuts import render, redirect
from django.views import View
from authentication.models import NewUserModel, labourmodels
from django.db.models import Q
from django.urls import reverse
from ecommerce.models import HireModel, ProductsModel, CartModel,RequestsModel
from .forms import AddStockForm, HireNowForm,Laboregisterform,PurchaseForm,AddPackageForm
from apps.home.models import Category,AppliedJobs,JobPaymentModel
from .forms import UpdateStockForm,CheckoutForm,UpdatePackageForm
from .models import HireModel, PackageModel, PurchaseModel, LabopaymentModel,RefundHistory
import datetime
from datetime import date, datetime
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import random,datetime
from apps.home.models import Category
from django.conf import settings
from django.views.decorators.cache import cache_control
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache

@method_decorator(login_required,name='dispatch')
class Home(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html', {})


@method_decorator(login_required,name='dispatch')
class Shop(View):
	template_name='shop/shop.html'
	def get(self, request, *args, **kwargs):
		sort=request.GET.get('orderby')
		if request.GET.get('orderby') is not None and request.GET.get('orderby') != '':
			if sort == 'atoz':
				product = ProductsModel.objects.all().order_by("Product_name")
			elif sort == 'ztoa':
				product = ProductsModel.objects.all().order_by("-Product_name")
			elif sort == 'latest':
				product = ProductsModel.objects.all().order_by("id")
			elif sort == 'oldest':
				product = ProductsModel.objects.all().order_by("-id")
		else:
			product = ProductsModel.objects.all()
		cart = CartModel.objects.all().filter(username=request.user.username).values_list("Product_name",flat=True)
		count = CartModel.objects.all().filter(username=request.user.username).count()
		print(settings.MEDIA_ROOT,"media roooooooooooot")
		data = {
		"product":product,
		'form':PurchaseForm(),
		'current_path':"Shop",
		'cart' : cart,
		'count' : count,
		

		}
		if product:
			return render(request, self.template_name, data)
		else:
			return render(request,'home/emptylaboshop.html',{'current_path':"Shop"})
	def post(self, request, *args, **kwargs):
		print("redirected")
		return redirect('shop')
@method_decorator(login_required,name='dispatch')
class CartView(View):
	template_name = 'shop/cart.html'
	
	def get(self, request, *args, **kwargs):
		products = list(CartModel.objects.filter(username=request.user.username).values())
		print(products,"-----------products=====")
		if not products:
			return render(request,'home/emptycart.html',{'current_path':"Cart" })
		else:
			totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))
			context = {
			"products":products,
			'form':CheckoutForm(),
			'current_path':"Cart" ,
			'totalPrice': totalPrice["Total__sum"],
			}	
			return render(request, self.template_name, context)
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
class DelFromCartView(View):
	def get(self, request, id):
		cartData = CartModel.objects.filter(product_id=id)
		cartData.delete()
		messages.success(request,"Successfully deleted !")
		return redirect('cart')



@method_decorator(login_required,name='dispatch')
class CheckoutView(View):
	
	template_name = 'shop/checkout.html'

	def get(self, request, *args, **kwargs):
		products = list(CartModel.objects.filter(username=request.user.username).values())
		totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))
		# items = list(PurchaseModel.objects.filter(username=request.user.username,status = 1).values_list('Prices',flat=True))[0]
		# print(items)
		context = {
		"products":products,
		'form':PurchaseForm(),
		'current_path':"Checkout" ,
		'totalPrice': totalPrice["Total__sum"],
		}	
		return render(request, self.template_name, context)
	@cache_control( no_cache=True, must_revalidate=True, no_store=True )
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			print("entered")
			form = PurchaseForm(request.POST)
			if form.is_valid():
					
					Prices = list(CartModel.objects.filter(username=request.user.username).values_list('Total',flat=True))
					Quantity = list(CartModel.objects.filter(username=request.user.username).values_list('Quantity',flat=True))
					n = random.randint(0,99999)
					request.session['order']= n
					request.session['Building']= request.POST['building']
					request.session['Street']= request.POST['street']
					request.session['Locality']= request.POST['locality']

					product_name = list(CartModel.objects.filter(username=request.user.username).values_list('Product_name',flat=True))
					# totalPrice = CartModel.objects.aggregate(Sum('Total'))
					totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))
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
					return redirect('payment',id)
			messages.error(request,"Form not valid ! ")
			return render(request,self.template, {'form': PurchaseForm(request.POST)})

		else:   
			return redirect('shop')
			
@method_decorator(login_required, name='dispatch')
class Invoice(View):
	template_name = 'shop/invoice.html'
	def get(self, request):
		products = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Product_name')[0]
		prices = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Prices')[0]
		quantity = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Quantity')[0]
		total = PurchaseModel.objects.filter(username=request.user.username, status = 3).values_list('Total')[0][0]
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
		filter=request.GET.get('filter')
		datajob = jobmodel.objects.values()
		if request.GET.get('filter') is not None and request.GET.get('filter') != '':
			job=jobmodel.objects.filter(id=filter).values_list("job_title")[0][0]
			data = labourmodels.objects.filter(Q(job_title=job)&Q(status=1)).exclude(username=request.user.username)		
		else:
			data = labourmodels.objects.filter(status=1).exclude(username=request.user.username)

		newdata = data	
		alreadyRequested = RequestsModel.objects.filter(Q(hirer= request.user.username) & Q(status=3))
		hiredata = HireModel.objects.filter(status=3)

		print('alreadyRequested')
		print(alreadyRequested)
		
		if alreadyRequested != None:
			for datas in newdata:
				for item in alreadyRequested:
					if datas.username == item.worker_name:
						newdata = newdata.exclude(username=item.worker_name)

		if hiredata != None :
			print("New")
			for datas in newdata:
				for item in hiredata:
					print("1")
					if datas.username == item.worker_name:
						newdata = newdata.exclude(username = item.worker_name)		
						print("2")


		fund = NewUserModel.objects.filter(username=request.user.username).values('wallet')
		users=NewUserModel.objects.all()
		work = HireModel.objects.all()
		datacategory=Category.objects.values()

		

		context = {
			'data': newdata,
			'current_path':"Request services",
			'fund': fund,
			"datacategory":datacategory,
			"datajob":datajob,
			"user":users,
			"work":work,
		}
		is_sub = NewUserModel.objects.filter(username=request.user).values_list('is_sub')[0][0]
		if is_sub == True or request.user.is_superuser:
			if newdata:
				return render(request, 'laboshop/labo-shop.html', context)
			else:
				return render(request,'home/emptylaboshop.html',{'current_path':"Laboshop"})
		else:
			messages.error(request,"Membership Required !")
			return redirect("membership")
		

@method_decorator(login_required,name='dispatch')
class LaboShopCategory(View):
	def get(self,request, *args, **kwargs):
		data=Category.objects.values()
		datajob = jobmodel.objects.values()
		context={ 
			"data":data,
			"datajob":datajob,
		}
		return render(request,'laboshop_categories.html',context)

@method_decorator(login_required,name='dispatch')
class Addproduct(View):
	template = 'addStock.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_superuser:
			
			form = AddStockForm
			context = { 
						'form': form,
						'data': 'Add Stock',
						'current_path':"Add Stock", 
					}
	
			return render(request,self.template,context)
		else:
			return render(request,'home/page-403.html')
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			
			form = AddStockForm(request.POST,request.FILES)
			print(request.FILES,"dfddjfdfjdfhjkhfdjkhfjkhdfkjdhjfhjkdf")
			if form.is_valid():
				print("55555555555555555555555555555555")
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
		cartDta = CartModel.objects.filter(Product_name = productData)
		if cartDta:
			cartDta.delete()
		messages.success(request,"Success !")
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
			context["media_url"] = settings.NEW_VAR
			context["Image"] = productData.Image    
			
			
			return render(request, 'updatestock.html', context)
	
	def post(self, request, *args, **kwargs):
		id = request.POST['id']
		if request.method == 'POST':


			updatedRecord = ProductsModel.objects.get(id=id)


			updatedRecord. Product_name = request.POST['Product_name']
			product_names = CartModel.objects.filter(product_id=id)
			for Product_name in product_names:
				Product_name.Product_name = request.POST['Product_name']
				Product_name.save()

			updatedRecord. Price = request.POST['Price']
			Prices = CartModel.objects.filter(product_id=id)
			for Price in Prices:
				Price.Price = request.POST['Price']
				Price.save()

			updatedRecord. Quantity = request.POST['Quantity']

			try:
				cart_image = CartModel.objects.filter(product_id=id)
				for image in cart_image:
					image.Image = request.FILES['Image']
					image.save()
						
				print("changeing")	
				updatedRecord. Image = request.FILES['Image']
				# print(cart_image)
			except Exception:	
				print("no image found")
			updatedRecord.save()
			messages.success(request,"Success!")
			return redirect('stocklist')
		else:
			form = UpdateStockForm()
		return redirect(request, 'stocklist')

@method_decorator(login_required,name='dispatch')
class ProductTable(View):
	template = 'stocktable.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_superuser:

			products = ProductsModel.objects.all().order_by('id')
			context = {
				'prod' : products,
				'current_path':"Stock Table" 
			}
			return render(request, self.template, context=context)
		else:
			return render(request,'home/page-403.html',{})

@method_decorator(login_required,name='dispatch')
class LaboRegister(View):
	template = 'laboregister.html'
	def get(self, request,id, *args, **kwargs):
		category = Category.objects.filter(id=id).values_list('category_name')[0][0]
		jobs = jobmodel.objects.filter(category=category).values()
		userjob= labourmodels.objects.filter(username=request.user).values_list('job_title',flat=True)
		# print("----",jobs,"6666666666666666666666666666666")
		form = Laboregisterform(initial=category,jobs=userjob)
		request.session['category'] = category
		context = {
			"form" : form,
			"jobs" : jobs,
			'current_path':"Apply Services" 
		}
		# if not request.user.is_superuser:
		return render(request, self.template,context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = Laboregisterform(request.POST,request.FILES)
			print(request.POST.get("image_link"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("job_title"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("rate"),"image linkkkkkkkkkkkkkk")
			print(request.POST.get("work_type"),"image linkkkkkkkkkkkkkk")
			print(form.errors,"errrrororororororoor")
			# labourmodels['username']=request.user.username
			job_title = request.POST.get('job_title')
			category = request.session['category']
			phone = request.POST.get("phone")
			form.fields['job_title'].choices = [(job_title, job_title)]
			# if form.is_valid():
				# print(form.cleaned_data,"ffffffffffffffffffffffffffff")
			# image_link = request.POST.get("image_link")
			image_link = form.cleaned_data.get("image_link")
			credential = form.cleaned_data.get("credential")
			job_title = request.POST.get("job_title")
			rate = request.POST.get("rate")
			work_type = request.POST.get("work_type")
			userjob= labourmodels.objects.filter(username=request.user).values_list('job_title',flat=True)
			print(userjob,"----------------")
			print(type(userjob),"----------------")
			if job_title in userjob:
				print("ind-----------------------0")
				messages.error(request,"You have already applied for this job !!")
				form = Laboregisterform(initial=category)
				return render(request, self.template, {'form': form})

			else:
				print("illa-----------------------0")
				# obj = labourmodels.objects.create(username=request.user,image_link=image_link,job_title=job_title,rate=rate,work_type=work_type,status = 2,job_certificate=credential)
				

				obj = labourmodels.objects.create(username=request.user,image_link=image_link,job_title=job_title,rate=rate,work_type=work_type,status = 2,job_certificate=credential,phone=phone)
				# obj.save()
				messages.success(request,"Success !")
			# print(obj,"55555555555555")
				return redirect('active_service')
			# else:
			# 	print(form.errors)    
			# 	return render(request, self.template, {'form': form})


@method_decorator(login_required,name='dispatch')
class Labocategories(View):
	template = 'labo_categories.html'
	def get(self, request, *args, **kwargs):
		data = Category.objects.all()
		job = jobmodel.objects.values_list("category",flat=True)
		# print(job,"====================================================")
		context = {	
			"data" : data,
			'current_path':"Register Services" ,
			 'MEDIA_ROOT':settings.NEW_VAR,
			 "job":job,

		}
		if data:
			total_work = labourmodels.objects.filter(Q(username=request.user.username)&((Q(status=1)|Q(status=2)|Q(status=3)))).count()
			if request.user.is_sub:
				if total_work < 5 :
					return render(request, self.template,context)
				else:
					messages.error(request,"Job Applying Limit Reached !!")
					return redirect("laboshop")
			else:
				messages.error(request,"Subscription Required !!")
				return redirect("workerview")
		else:
			return render(request, "home/emptyworkerpage.html", context)

@method_decorator(login_required,name='dispatch')
class ActiveServices(View):
	def get(self, request, *args, **kwargs):
		data = labourmodels.objects.filter(Q(username = self.request.user.username) & (Q(status=0) | Q(status=1) | Q(status=2))).order_by("id")
		user = NewUserModel.objects.all()
		context = {
			"data" : data,
			"user" : user,
			'current_path':"ActiveServices"
		}
		if request.user.is_sub:
			if data:
					return render(request,'activeServices.html',context)
			else:
				return render(request,"home/emptyworkerservices.html",context)
		else:
			messages.error(request,"Subscription Required !!")
			return redirect('workerview')

@method_decorator(login_required,name='dispatch')
class HireNowView(View):
	def get(self, request,id, *args, **kwargs):
		data = {
			"id":id,
		}
		form = HireNowForm(data)
		context = {'form': form}
		return render(request, "hireNowForm.html",context)
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = HireNowForm(request.POST)
			id = request.POST.get("id")
			name = request.user.first_name +" "+ request.user.last_name
			place = request.POST.get("Place")
			phone = request.POST.get("Phone")
			work_type = request.POST.get("Work_mode")
			worker_phone = labourmodels.objects.filter(id=id).values_list("phone")[0][0]
			worker_name = labourmodels.objects.filter(id=id).values_list("username")[0][0]
			job_title = labourmodels.objects.filter(id=id).values_list("job_title")[0][0]
			rate = labourmodels.objects.filter(id=id).values_list("rate")[0][0]

			if form.is_valid():
				n = random.randint(0,99999)
				obj = RequestsModel.objects.create(
					id=n,
					hirer=request.user.username,
					name=name,
					place=place,
					work_type=work_type,
					phone=phone,
					status=0,
					job_title=job_title,
					rate=rate,
					worker_name=worker_name,
					worker_phone=worker_phone,
					created_at=datetime.datetime.now().date())
				# k = request.POST.get("id")
				print(obj)
				pay = LabopaymentModel.objects.create(work_id=obj,rate=rate,status=0,amount=0)				
				return render(request,'home/hirenowpay.html',{"id":n,"rate":rate})
			else:
				messages.error(request,'Unsuccesfull')
				return redirect('laboshop')
@method_decorator(login_required, name='dispatch')
class Userpayments(View):
	def get(self, request,id, *args, **kwargs):
		wallet_balance =request.user.wallet
		user_id=id
		rate = AppliedJobs.objects.filter(id=id).values_list("rate")[0][0]
		print(rate,"rateeeeeeeeeeeeeeeeeeeeeeeeeeeee")
		if wallet_balance >= rate:
			NewUserModel.objects.filter(username=request.user.username).update(wallet=wallet_balance-rate)	
			AppliedJobs.objects.filter(id=id).update(status=1)
			JobPaymentModel.objects.filter(work_id=id).update(status=1,amount=rate)
			messages.success(request,'Payment Successful')
			return redirect('jobrequests')
		else:
			messages.error(request,'Payment Failed')
			return redirect('jobrequests')
@method_decorator(login_required, name='dispatch')
class HireNowPayments(View):
	def get(self, request,id, *args, **kwargs):
		wallet_balance =request.user.wallet
		rate = LabopaymentModel.objects.filter(work_id=id).values_list("rate")[0][0]
		if wallet_balance >= rate:
			NewUserModel.objects.filter(username=request.user.username).update(wallet=wallet_balance-rate)
			RequestsModel.objects.filter(id=id).update(status=3)
			LabopaymentModel.objects.filter(work_id=id).update(status=1,amount=rate)
			messages.success(request,'Payment Successful')
			return redirect('laboshop')
		else:
			messages.error(request,'Payment Failed')
			return redirect('laboshop')


@method_decorator(login_required,name='dispatch')
class CancelRequest(View):
	def get(self, request,id):
		requests = RequestsModel.objects.filter(id=id).first()
		rate = requests.rate
		user = NewUserModel.objects.filter(username=requests.hirer)
		wallethirer= user.first().wallet
		user.update(wallet=wallethirer+rate)
		

		requests.delete()
		messages.success(request,"Request Cancelled Successfully !")
		return redirect('requested')
@method_decorator(login_required,name='dispatch')
class Assignedworks(View):
	template_name = 'assigned_works.html'
	def get(self, request, *args, **kwargs):
		services = RequestsModel.objects.filter(worker_name = request.user.username,status=3)
		context = {
			"data": services,
			'current_path':"Assigned Services"
		}
		if request.user.is_sub:
			if services:
				return render(request,self.template_name,context)
			else:
				return render(request,'home/emptyworkerservices.html',context)
		else:
			messages.error(request,"Subscription Required !! ")
			return redirect("workerview")
@method_decorator(login_required,name='dispatch')
class Acceptservice(View):
	def get(self,request,id, *args, **kwargs):
		# serviceobj = HireModel.objects.get(id=id)
		# status = RequestsModel.objects.filter(id=id).values_list("status")[0][0]
		# print(status,"----sbsjdsdsldsldshdshldhsdh-----") 
		# if status == 3:
		job = RequestsModel.objects.filter(id=id).values_list("job_title")[0][0]


		labo_job = labourmodels.objects.filter(Q(username=request.user)&Q(job_title=job))
		print(labo_job)
		labo_job.update(status=0)
		RequestsModel.objects.filter(id=id).update(status=1)
		messages.success(request, "Accepted Successfully!!")
		return redirect('assigned')
		# elif status ==2:
		# 	return redirect('laboshop')
		# else:
		# 	return redirect('labocategory')
@method_decorator(login_required,name='dispatch')	
class Togglestatus(View):
	def get(self, request,id, *args, **kwargs):
		status = labourmodels.objects.filter(id=id).values_list("status")[0][0]

		# print(status,":::::::::::::::::::::::")
		if status == 0:
			total_work = labourmodels.objects.filter(Q(username=request.user.username)&((Q(status=1)|Q(status=2)|Q(status=3)))).count()
			if total_work <5:
				hire = HireModel.objects.filter(Q(worker_name=request.user)&Q(status=3)).values()
				if not hire.exists():
					labourmodels.objects.filter(id=id).update(status=1)
					messages.success(request,"Success !")
					# print("hireeeeeeeeeeeeeeeeee")
					return redirect("active_service")
				else:
					messages.error(request,"Pending Job Found! ")
					# print("hireeeeeeeeeeeeeeeeee")
					# print("someting in query")
					return redirect("active_service")
				
			else:
				messages.error(request,"Maximum Job Limit Reached !!!")
				return redirect("active_service")
		elif status ==1:
			labourmodels.objects.filter(id=id).update(status=0)
			messages.success(request,"Success !")
			return redirect("active_service")
		elif status ==2:
			labourmodels.objects.filter(id=id).delete()
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
				walletadmin =NewUserModel.objects.filter(username="admin").first()
				NewUserModel.objects.filter(username="admin").update(wallet=walletadmin.wallet+packagecost)	
				
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
@method_decorator(login_required, name='dispatch')
class Payment(View):
	template_name= 'shop/payment.html'
	def get(self, request, id, *args, **kwargs):
		products= PurchaseModel.objects.filter(id=id).values_list('Product_name')[0]
		prices = PurchaseModel.objects.filter(id=id).values_list('Prices')[0]
		quantity = PurchaseModel.objects.filter(id=id).values_list('Quantity')[0]
		total= PurchaseModel.objects.filter(id=id).values_list('Total')[0][0]
		context={
			"total":total,
			"products":products,
			"prices":prices,
			"id":id,
			"quantity":quantity,

		}
		return render(request,self.template_name,context)
@method_decorator(login_required, name='dispatch')
class ConfirmPay(View):
	
	@cache_control( no_cache=True, must_revalidate=True, no_store=True )
	def get(self, request,id, *args, **kwargs):
		product_id = CartModel.objects.filter(username=request.user.username).values_list("product_id")
		for j in product_id:
				quantity = CartModel.objects.filter(product_id=j[0]).values_list("Quantity")[0][0]
				quant = ProductsModel.objects.filter(id=j[0]).values_list("Quantity")[0][0]
				a = ""
				if quant>=quantity:
					pass
				else:
					product = CartModel.objects.filter(product_id=j[0]).values_list("Product_name")[0][0]
					a+=product


					messages.error(request,"Sorry , "+ a +" are unavailable at the moment !!")
					return redirect("cart")
		for k in product_id:
			quantity = CartModel.objects.filter(product_id=k[0]).values_list("Quantity")[0][0]
			quant = ProductsModel.objects.filter(id=k[0]).values_list("Quantity")[0][0]			
			ProductsModel.objects.filter(id=k[0]).update(Quantity=quant-quantity)
		wallet_balance = NewUserModel.objects.filter(username=request.user.username).values_list("wallet")[0][0]
		total_price=PurchaseModel.objects.filter(id=id).values_list("Total")[0][0]
		if wallet_balance >= total_price:
			adminwallet =  NewUserModel.objects.get(username = 'admin')
			adminbalance = NewUserModel.objects.filter(username = 'admin').values_list('wallet',flat=True)[0]
			print(adminbalance)
			adminwallet.wallet = adminbalance + total_price
			adminwallet.save()
			NewUserModel.objects.filter(username=request.user.username).update(wallet=wallet_balance-total_price)
			PurchaseModel.objects.filter(id=id).update(status=3)
			obj = CartModel.objects.filter(username=request.user.username)
			# product_id = CartModel.objects.filter(username=request.user.username).values_list("product_id")
			# for i in product_id:
			# 	quantity = CartModel.objects.filter(product_id=i[0]).values_list("Quantity")[0][0]
			# 	quant = ProductsModel.objects.filter(id=i[0]).values_list("Quantity")[0][0]
			# 	ProductsModel.objects.filter(id=i[0]).update(Quantity=quant-quantity)
			obj.delete()
			return redirect("invoice")
		else:
			messages.error(request,"Not enough balance in wallet!!")
			PurchaseModel.objects.filter(id=id).update(status=2)
			return redirect("payment",id)

@method_decorator(login_required, name='dispatch')
class Packages(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_superuser:
			template = 'packages.html'
			package = PackageModel.objects.all()
			context = {
				"package":package,
				'MEDIA_ROOT':settings.NEW_VAR,
				'current_path':'Packages List'
			}
			return render(request,template,context)
		else:
			return render(request,'home/page-403.html')

@method_decorator(login_required,name='dispatch')
class Deletepackage(View):
	def get(self, request, id):
		packageData = PackageModel.objects.get(id=id)
		userwpackage = NewUserModel.objects.filter(package=id).count()
		# print(userwpackage,"existing package of users!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		if userwpackage!=0:
			messages.error(request,"There are users with that package  !")
			return redirect('packages')
		else:
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
			updatedRecord. image = request.FILES['image']
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
		if request.user.is_superuser:

			form = AddPackageForm()
			context = { 
						'form': form,
						'data': 'Add Package',
						'current_path':"Add Package", 
					}
	
			return render(request,self.template,context)
		else:
			return render(request, 'home/page-403.html')
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = AddPackageForm(request.POST,request.FILES)
			print(request.FILES)
			print("--------------------------")
			print(request.POST.get('package_name'))
			print(request.POST.get('validity'))
			print(request.POST.get('cost'))
			print(request.POST.get('image'))
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

@method_decorator(login_required, name='dispatch')
class membership(View):
	def get(self, request, *args, **kwargs):
		template = "membership_card.html"
		data = PackageModel.objects.all()
		if data:
			context={
				"data": data,
			}
			return render(request,template,context)
		else:
			return render(request,"home/emptypackage.html")
@method_decorator(login_required, name='dispatch')
class Workerview(View):
	def get(self, request, *args, **kwargs):
		reqcount = RequestsModel.objects.filter(Q(worker_name=request.user)&Q(status=3)).count()
		revenue = HireModel.objects.filter(Q(worker_name=request.user)&Q(status=4)).values_list("rate")
		a = 0
		for i in revenue:
			a+=i[0]
		refund = RefundHistory.objects.filter(worker=request.user).values_list("worker_refund")
		for j in refund:
			a+=j[0]
		tot_work = HireModel.objects.filter(Q(worker_name=request.user)&Q(status=4)).count()
		context ={
			"current_path":'',
            "req" :reqcount,
            "rev": a,
			"tot" :tot_work,
        }
		return render(request,'home/dashboard1.html',context)

@method_decorator(login_required, name='dispatch')
class Individual(View):
	def get(self, request, *args, **kwargs):
		template = 'individualprofile.html'
		return render(request,template,{})
@method_decorator(login_required, name='dispatch')
class RefundHistoryUser(View):
	def get(self, request, *args, **kwargs):
		template = 'refundhistoryuser.html'
		refund = RefundHistory.objects.filter(hirer=request.user).values()
		context = {
			"refund":refund,
			'current_path': "Refund history",
		}
		if refund:
			return render(request,template,context)
		else:
			return render(request,"home/emptypage.html", context)
@method_decorator(login_required, name='dispatch')
class RefundHistoryWorker(View):
	def get(self, request, *args, **kwargs):
		template = 'refundhistoryworker.html'
		refund = RefundHistory.objects.filter(worker=request.user).values()
		context = {
			"refund":refund,
			'current_path': "Refund history",
		}
		if refund:
			return render(request,template,context)
		else:
			return render(request,"home/emptyworkerpage.html",context)

@method_decorator(login_required,name='dispatch')
class LaboTransactions(View):
	def get(self, request, *args, **kwargs):
		work = HireModel.objects.filter(worker_name=request.user).filter(status__in=[4, 5]).order_by('id')
		context = {
            'work': work,
            'current_path': "Laboshop History"
        }
		if work:
			return render(request,'labotransaction.html',context)
		else:
			return render(request,"home/emptyworkerpage.html",context)	

@method_decorator(login_required,name='dispatch')
class AdminTransactions(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_superuser or request.user.is_staff:
			purchase = PurchaseModel.objects.all().values().exclude(status__in=[2,1,0])
			packages = PurchaseModel.objects.filter(status=0).values()
			hire = HireModel.objects.filter(status__in = [4,5])
			refund = RefundHistory.objects.all().values()
			print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",purchase)
			# print("ppppppppppppppppppppppppppppppppppppppppppppppppppppppppp",purchase.username)
			context = {
				'purchase': purchase,
				'hire':hire,
				'refund':refund,
				'current_path':'Transactions',
				'package':packages
			}
			return render(request,'home/adminTransactions.html',context)
		else:
			return render(request,'home/page-403.html')

class SearchProducts(View):
	template_name='shop/items_list.html'
	def post(self,request, *args, **kwargs):
		search_tag = request.POST['search_keyword']
		filterdData = ProductsModel.objects.filter(Product_name__icontains = search_tag)
		context = {'search_result': filterdData}
		return render(request ,self.template_name,context)


@method_decorator(login_required,name='dispatch')
class DecreaseNo(View):
	def post(self,request, *args, **kwargs):
		p_id = request.POST['p_id']
		print(p_id)
		price = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Price')[0][0]
		quantity = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Quantity')[0][0]
		print(price,quantity)
		total = (quantity - 1 ) * price
		if quantity <= 1:
			messages.error(request,"Error !")
			return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

		else:
			CartModel.objects.filter(product_id=p_id,username= request.user.username).update(Quantity = quantity - 1, Total = total )
			p_qty = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Quantity')[0][0]
			totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))

			data = 	{'status':'success',
					'p_qty':p_qty,
					'p_total':total,
					'totalPrice': totalPrice["Total__sum"],
					}
			from django.http import JsonResponse
			return JsonResponse(data)


@method_decorator(login_required,name='dispatch')
class IncreaseNo(View):
	template_name = 'shop/cart.html'
	def post(self, request, *args, **kwargs):

		p_id = request.POST['p_id']
		print(p_id)
		print("Incrementing")
		price = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Price')[0][0]
		quantity = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Quantity')[0][0]
		product = CartModel.objects.filter(product_id=p_id,username=request.user.username).values_list("Product_name")[0][0]
		available_qnty = ProductsModel.objects.filter(Product_name=product).values_list("Quantity")[0][0]
		if (available_qnty-quantity) > 0:
			total = (quantity + 1 ) * price
			print("toal product price",quantity)
			print("toal product price",int(price))
			print("toal product price",total)
			products = list(CartModel.objects.filter(username=request.user.username).values())
			CartModel.objects.filter(product_id=p_id,username= request.user.username).update(Quantity = quantity + 1 ,  Total= total)
			totalPrice = CartModel.objects.filter(username = request.user.username).aggregate(Sum('Total'))
			p_qty = CartModel.objects.filter(product_id=p_id,username= request.user.username).values_list('Quantity')[0][0]
			data = 	{'status':'success',
					'p_qty':p_qty,
					'p_total':total,
					'totalPrice': totalPrice["Total__sum"],
					}
			from django.http import JsonResponse
			return JsonResponse(data)
		else:
			messages.error(request,"Not enough available stock !")
			return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
