from multiprocessing import context
from tempfile import template
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ecommerce.models import HireModel, PurchaseModel
from .forms import AddJobForm, CategoryForm ,JobPostingForm ,AddFundForm,ApplyForm
from .models import Category,JobPostingModel   
from django.contrib import messages
from django.urls import reverse
from authentication.models import jobmodel,NewUserModel,labourmodels
from django.views.generic import ListView
from django.db.models import Q
import pdb


# Create your views here.
@method_decorator(login_required,name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/dashboard.html")
@method_decorator(login_required,name='dispatch')
class FundView(View):
    template = 'home/fund-management.html'
    template2 = 'home/page-403.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            context ={'current_path':"Fund Deposit" }
            context['form'] = AddFundForm(request=request)
            return render(request, self.template, context)
        else:
            return render(request, self.template2)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AddFundForm(request.POST,request=request)
            if form.is_valid():
                form.save()
                return redirect(reverse('funds'))
            else:    
                return render(request, self.template, {'form': form})

        else:

            return render(request, self.template, {'form': form})

@method_decorator(login_required,name='dispatch')
class TransactionView(ListView):
        model =  PurchaseModel
        context_object_name = 'datas'
        template_name = 'home/transactions.html'
        def get_queryset(self):
            new_context = PurchaseModel.objects.filter(status=3)
            return new_context

@method_decorator(login_required,name='dispatch')
class Userservices(View):
    def get(self, request, *args, **kwargs):
        details = HireModel.objects.filter (Hire_name = request.user).order_by('id')
        context ={
            'details': details,
            'current_path': "User Services"
        }
        return render(request, "home/user-services.html",context)

@method_decorator(login_required,name='dispatch')
class Workerservices(View):
    def get(self, request,*args, **kwargs):
        work = HireModel.objects.filter (worker_name = request.user).order_by('id')
        context = {
            'work' : work,
            'current_path' : "Worker Services"
        }
        return render(request, "home/worker-services.html", context)


class LookForJobs(View):
    def get(self, request,*args, **kwargs):
        look = JobPostingModel.objects.filter(status = 0).values()
        context = {
            'look' : look
        }
        return render(request, "home/lookforjobs.html", context)


class ApplyFormView(View):
    def get(self, request,*args, **kwargs):
       
        id = kwargs.get('id')
        maindata = JobPostingModel.objects.filter(id=id).first()
        hire = JobPostingModel.objects.filter(id=id).values_list('hirer')[0][0]
        print(hire,"jggggggggggggggggggggggggggggggg")
        data = {
            'name': maindata.name,
            'hirer': hire,
            'place': maindata.place,
            'work_type': maindata.work_type,
            'phone': maindata.phone,
            'status': maindata.status,
            'job_title': maindata.job_title,
            'worker_name': request.user.username,
            'worker_phone': request.user.phone_no
        }
        form = ApplyForm(data)
        return render(request, "home/applyform.html", {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ApplyForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Success")
                return redirect('shop')
            else:
                messages.error(request,"error")
                return redirect('shop') 
        return redirect(request, 'shop') 

@method_decorator(login_required,name='dispatch')
class CompletedService(View):
    def get(self, request, *args, id , **kwargs):
        user= HireModel.objects.get(id=id)
        if user.worker_status:
            user.save()
        else:
            user.worker_status = True
            user.save()
        return redirect('userservices')

@method_decorator(login_required,name='dispatch')
class UserCompletedService(View):
     def get(self, request, *args, id , **kwargs):
        data= HireModel.objects.get(id=id)
        if data.user_status:
            data.save()
        else:
            data.user_status = True
            data.save()
        return redirect('workerservices')

@method_decorator(login_required,name='dispatch')
class ServiceView(View):
    def get(self, request, *args, **kwargs):
        data = HireModel.objects.filter (Hire_name = request.user)
        context = {'data': data ,'current_path':"Requested Services" }
        return render(request, "home/requested-services.html",context)

class RatingView(View):
    def get(self, request, *args,id, **kwargs):
        details = HireModel.objects.get(id=id)
        context = {
			'details': details,
		}
        return render(request, "home/rating.html",context)


class Ratings(View):
    def get(self, request, *args, id, **kwargs):
        star = id
        data = HireModel.objects.get(Hire_name = request.user)
        data.rating = star
        data.worker_status = True
        data.save()
        return redirect('userservices')



        
@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self, request, *args, **kwargs):
        tables = Category.objects.all()
        jobs = jobmodel.objects.all()
        context = {
            'tables': tables ,
            'current_path':"Categories",
            'data': jobs
            }
        return render(request, "home/category.html",context)


@method_decorator(login_required,name='dispatch')
class AddCategoryView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm
        context = {'form': form ,'current_path':"Add Category" }
        return render(request, "home/add_categoryform.html",context)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Category added successfully")
                return redirect('category')
            else:
                messages.error(request,"error")
        return redirect(request, 'add_category')


@method_decorator(login_required,name='dispatch')
class DeleteCategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request,"Category Deleted")
        return redirect('category')
    


@method_decorator(login_required,name='dispatch')
class Addjobsview(View):
    template = 'home/addjob.html'
    def get(self, request, *args, **kwargs):
        # category = Category.objects.all().values_list('category_name')
        # # jobs = jobmodel.objects.filter(category=category).values()
		# # print("----",jobs,"6666666666666666666666666666666")
        form = AddJobForm()
        context = {
			"form" : form,
			'current_path':"Apply Services" 
		}
		# if not request.user.is_superuser:
        return render(request, self.template,context)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AddJobForm(request.POST)
            job_name = request.POST['job_name']
            category = request.POST['category']
            form.fields['category'].choices = [(category, category)]
            obj = jobmodel.objects.create(job_title=job_name,category=category)
            return redirect(reverse('category'))
        else:    
            return render(request, self.template, {'form': form})
        # else:
        #     return render(request, self.template, {'form': form})

@method_decorator(login_required,name='dispatch')
class Deletejob(View):
    def get(self, request, id):
        job = jobmodel.objects.get(id=id)
        job.delete()
        messages.success(request,"Job Deleted")
        return redirect('category')
    
class Access_denied(View):
    template_name = ' home/page403.html  '
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

class ManageUser(View):
    def get(self, request, *args,**kwargs):
        details = NewUserModel.objects.all().order_by('id').exclude(username='admin')
        context = {
            'details': details ,
            'current_path':"Manage User",
            }
        return render(request, "home/manage-user.html",context)

class UpdateUser(View):
    def get(self, request,id, *args, **kwargs):
        user= NewUserModel.objects.get(id=id)
        if user.is_active:
            user.is_active=False
            user.save()
        else:
            user.is_active = True
            user.save()
        # print(users)
        return redirect('manageuser')



class JobPostingView(View):
    template_name = 'home/job-posting.html'
    def get(self, request,id, *args, **kwargs):
        category = Category.objects.filter(id=id).values_list('category_name')[0][0]
        jobs = jobmodel.objects.filter(category=category).values()
        # print("----",jobs,"6666666666666666666666666666666")
        form = JobPostingForm(initial=category,user=request.user.username)
        context = {
        "form" : form,
        "jobs" : jobs,
        'current_path':"Apply Services" 
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = JobPostingForm(request.POST)
            try:
                obj = JobPostingModel.objects.create(
                    hirer=request.user.username,
                    place=request.POST['place'],
                    job_title=request.POST['job_title'],
                    work_type=request.POST['work_type'],
                    phone=request.POST['phone'],
                    name=request.POST['name'])
                obj.save()
                return redirect('laboshop')

            except Exception :
                return redirect('shop')


            else:
                print("not valid")    
                return redirect('shop')

class ManageServices(View):
    def get(self, request, *args,**kwargs):
        details = labourmodels.objects.all().exclude(status=3).order_by('id')
        context = {
            'details': details ,
            'current_path':"Manage Services",
            }
        return render(request, "home/manage_services.html",context)

class UpdateServices(View):
    def get(self, request,id, *args, **kwargs):
        status=labourmodels.objects.filter(id=id).values_list("status")[0][0]
        if status == 0:
            labourmodels.objects.filter(id=id).update(status=1)
            messages.success(request,"Success !")
            return redirect("manageservices")
        elif status == 1:
            labourmodels.objects.filter(id=id).update(status=0)
            messages.success(request,"Success !")
            return redirect("manageservices")
        else:
            labourmodels.objects.filter(id=id).update(status=0)
            messages.success(request,"Success !")
            return redirect("manageservices")

@method_decorator(login_required,name='dispatch')
class Labocategories2(View):
	template = 'home/labo-category2.html'
	def get(self, request, *args, **kwargs):
		data = Category.objects.all()
		context = {	
			"data" : data,
			'current_path':"Provide Jobs" 
		}
		total_work = JobPostingModel.objects.filter(Q(hirer=request.user.username)&((Q(status=1)|Q(status=2)|Q(status=3)))).count()

		if total_work < 5 :
			return render(request, self.template,context)
		else:
			messages.error(request,"Job Applying Limit Reached !!")
			return redirect("laboshop")


@method_decorator(login_required,name='dispatch')
class ServiceRequests(View):
    def get(self, request,*args, **kwargs):
        details = labourmodels.objects.filter(status=3).order_by('id')
        context = {
            'details': details ,
            }
        return render(request, "home/service_requests.html",context)

@method_decorator(login_required,name='dispatch')
class PendingKYC(View):
    template_name = 'home/pending-registration-requests.html'
    def get(self, request,*args, **kwargs):
        datas = NewUserModel.objects.filter(kyc_approved=0).order_by('id')
        context = {
            'media_url':settings.NEW_VAR,
            'datas': datas ,
             'current_path':"Pending KYC  ",
            }
        return render(request, self.template_name,context)



class AcceptServices(View):
    def get(self, request,id, *args, **kwargs):
        status=labourmodels.objects.filter(id=id).values_list("status")[0][0]
        labourmodels.objects.filter(id=id).update(status=1)
        messages.success(request,"Success !")
        return redirect("servicerequests")

class RejectServices(View):
    def get(self, request, id):
        data = labourmodels.objects.get(id=id)
        data.delete()
        messages.success(request,"Cancelled")
        return redirect('servicerequests')
    
       
class ApproveUser(View):
    def get(self, request,  id):
       try:
        user = NewUserModel.objects.get(id=id)
        user.kyc_approved=True
        user.save()
        messages.success(request ,"Approved User.") 
        return redirect('pendingkyc')
       except Exception as e :
        messages.error(request ,"An error occured during the approval.") 
