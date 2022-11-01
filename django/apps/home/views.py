from multiprocessing import context
from tempfile import template
from django.shortcuts import render,redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ecommerce.models import HireModel, PurchaseModel
from .forms import AddJobForm, CategoryForm ,JobPostingForm ,AddFundForm
from .models import Category,JobPostingModel   
from django.contrib import messages
from django.urls import reverse
from authentication.models import jobmodel,NewUserModel
from django.views.generic import ListView


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
            new_context = PurchaseModel.objects.filter(status=0)
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
        details = NewUserModel.objects.all().order_by('id')
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
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
