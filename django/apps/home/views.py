from multiprocessing import context
from tempfile import template
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ecommerce.models import HireModel, PurchaseModel,RequestsModel,RefundHistory,PackageModel
from .forms import AddJobForm, CategoryForm, JobPostingForm, AddFundForm, ApplyForm,CommentForm
from .models import Category, JobPostingModel, AppliedJobs,Category,JobPaymentModel,CitiesModel,ReeportModel
from django.contrib import messages
from django.urls import reverse
from authentication.models import jobmodel, NewUserModel, labourmodels
from django.views.generic import ListView
from django.db.models import Q
import pdb
import datetime
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):

        req_count = HireModel.objects.filter(Q(Hire_name=request.user)&(Q(status=4)|Q(status=5))).count()
        purchase = PurchaseModel.objects.filter(username=request.user).values_list("Total")
        sub_at=request.user.subscribed_at
        a = datetime.datetime.now().date()
         
        if sub_at != None:
            diff = a-sub_at
            validity = PackageModel.objects.filter(id=request.user.package).values_list("validity")[0][0]

            tot_purchase = 0
            for i in purchase:
                tot_purchase += i[0]

            context ={
                "req" : req_count,
                "tot" : tot_purchase,
                "exp" : validity-diff.days, 
                "current_path":"",
            }
        else:
            tot_purchase = 0
            for i in purchase:
                tot_purchase += i[0]
            context ={
                "req" : req_count,
                "tot" : tot_purchase,
                "current_path":"",
            }


        
        return render(request, "home/dashboard.html",context)


@method_decorator(login_required, name='dispatch')
class FundView(View):
    template = 'home/fund-management.html'
    template2 = 'home/page-403.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            context = {'current_path': "Fund Deposit"}
            context['form'] = AddFundForm(request=request)
            return render(request, self.template, context)
        else:
            return render(request, self.template2)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AddFundForm(request.POST, request=request)
            if form.is_valid():
                form.save()
                messages.success(request,"Added fund successfully!!!")
                return redirect(reverse('funds'))
            else:
                messages.error(request,"Not Valid !!" )
                return render(request, self.template, {'form': form})

        else:

            return render(request, self.template, {'form': form})


@method_decorator(login_required, name='dispatch')
class TransactionView(View):
    template_name = 'home/transactions.html'
    def get(self, request,  *args, **kwargs):
            new_context = PurchaseModel.objects.filter(
            status=3, username=request.user.username)
            context={'datas' : new_context} 
            if request.user.is_superuser:
                new_context = PurchaseModel.objects.filter(
                status=3).exclude(username=request.user.username)
                context={
                    'datas' : new_context,
                    'current_path': "Transactions"
                    }
                if new_context: 
                    return render(request , self.template_name , context)
                else:
                    messages.success(request,"No Transactions Found")
                    return render(request, "home/emptyadmin.html",context)
            else:
                new_context = PurchaseModel.objects.filter(
                status=3,username=request.user.username)  
                context={
                    'datas' : new_context,
                    'current_path': "Transactions"
                    } 
                if new_context:
                    return render(request , self.template_name , context)   
                else:
                    messages.success(request,"No Transactions Found")
                    return render(request, "home/emptypage.html",context)
@method_decorator(login_required, name='dispatch')
class Userservices(View):
    def get(self, request, *args, **kwargs):
        details = HireModel.objects.filter(
            Hire_name=request.user).order_by('id').exclude(status__in=[4,5])
        context = {
            'details': details,
            'current_path': "User Services"
        }
        if details:
            return render(request, "home/user-services.html", context)
        else:
            return render(request, "home/emptyservices.html",context)
    def post(self, request, *args,  **kwargs):
        if request.method == 'POST':
            # print(hireid,"hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            print(request.POST.get('id'))
            id=request.POST.get('id')
            
            if ReeportModel.objects.filter(username=request.user,hireid=id).exists():
                messages.error(request,"Sorry Already Reported The Issue, Wait For it To Process  !")
                return redirect("userservices")
            print(request.POST.get('email_address'))
            email=request.POST.get('email_address')
            print(request.POST.get('phone_number'))
            ph=request.POST.get('phone_number')
            print(request.FILES.get('image_proof'))
            img=request.FILES.get('image_proof')
            print(request.POST.get('issue_reported'))
            issue=request.POST.get('issue_reported')
            obj=ReeportModel.objects.create(username=request.user.username,woh=0,hireid=id,email=email,phone=ph,issue=issue,proof=img)
            obj.save()
            messages.success(request,"Successfully Reported The Issue ")
            return redirect("userservices")


        

@method_decorator(login_required, name='dispatch')
class Workerservices(View):
    def get(self, request, *args, **kwargs):
        work = HireModel.objects.filter(
        worker_name=request.user).order_by('id').exclude(status__in=[4,5])
        context = {
            'work': work,
            'current_path': "Worker Services"
        }
        if work:
            return render(request, "home/worker-services.html", context)
        else:
            return render(request, "home/emptyworkerservices.html",context)
    def post(self, request, *args,  **kwargs):
        if request.method == 'POST':
            # print(hireid,"hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            print(request.POST.get('id'))
            id=request.POST.get('id')
            
            if ReeportModel.objects.filter(username=request.user,hireid=id).exists():
                messages.error(request,"Sorry Already Reported The Issue, Wait For it To Process  !")
                return redirect("workerservices")
            print(request.POST.get('email_address'))
            email=request.POST.get('email_address')
            print(request.POST.get('phone_number'))
            ph=request.POST.get('phone_number')
            print(request.FILES.get('image_proof'))
            img=request.FILES.get('image_proof')
            print(request.POST.get('issue_reported'))
            issue=request.POST.get('issue_reported')
            obj=ReeportModel.objects.create(username=request.user.username,woh=1,hireid=id,email=email,phone=ph,issue=issue,proof=img)
            obj.save()
            messages.success(request,"Successfully Reported The Issue ")
            return redirect("workerservices")

@method_decorator(login_required, name='dispatch')

class ApplyFormView(View):
    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')
        maindata = JobPostingModel.objects.filter(id=id).first()
        data = {
            'name': maindata.name,
            'hirer': maindata.hirer,
            'place': maindata.place,
            'work_type': maindata.work_type,
            'phone': maindata.phone,
            'status': 0,
            'job_title': maindata.job_title,
            'worker_uname': request.user.username,
            'worker_name': request.user.first_name+ " " + request.user.last_name,
            'worker_phone': request.user.phone_no,
            'current_path': "Apply for job"

        }
        form = ApplyForm(data)
        return render(request, "home/applyform.html", {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            applied = AppliedJobs.objects.filter(Q(worker_uname=request.user.username)&Q(hirer=request.POST.get("hirer"))&Q(job_title=request.POST.get("job_title"))).exists()
            # print(applied,"exists or notttttttttttt")
            if applied:
                messages.error(request, "Already applied for this job !!")
                return redirect('lookforjobs')
            else:
                rate = request.POST['rate']
                form = ApplyForm(request.POST)
                if form.is_valid():
                    obj = form.save()
                    pay = JobPaymentModel.objects.create(work_id=obj,rate=rate,status=0,amount=0)				
                    messages.success(request, "Job Applied Successfully")
                    return redirect('lookforjobs')
                else:
                    messages.error(request, "Application Failed")
                    return redirect('lookforjobs')
        else:
            messages.error(request, "error")
            # return redirect('shop')
            return redirect(request, 'lookforjobs')


@method_decorator(login_required, name='dispatch')
class UnCompletedService(View):
    def get(self, request, *args, id, **kwargs):
        user = HireModel.objects.get(id=id)
        if user.worker_status:
            messages.error(request,"Sorry The Service Is Completed,   Unable To Cancel !!")
            return redirect('userservices')
        else:
            user.user_status = 2
            user.save()
            return redirect('userservices')

@method_decorator(login_required, name='dispatch')
class CompletedService(View):
    def get(self, request, *args, id, **kwargs):
        user = HireModel.objects.get(id=id)
        if user.status == 4:
            user.save()
        elif user.worker_status:
            user.save()
        else:
            user.worker_status=True
            user.save()
        return redirect('workerservices')


@method_decorator(login_required, name='dispatch')
class UserCompletedService(View):
    def get(self, request, *args, id, **kwargs):
        data = HireModel.objects.get(id=id)
        if data.status == 4:
            data.save()
        elif data.user_status == 1:
            data.save()
        else:
            data.user_status = 1
            data.save()
        return redirect('userservices')


@method_decorator(login_required, name='dispatch')
class ServiceView(View):
    template_name = "home/requested-services.html"
    def get(self, request, *args, **kwargs):
        data = RequestsModel.objects.filter(
            hirer   =request.user).exclude(status__in=[0,2,5])
        context = {'data': data, 'current_path': "Requested Services"}
        if data:
            return render(request, self.template_name, context)
        else:
            return render(request, "home/emptyservices.html", context)
@method_decorator(login_required, name='dispatch')
class RatingView(View):
    def get(self, request, *args, id, **kwargs):
        details = HireModel.objects.get(id=id)
        form =CommentForm()
        context = {
            'details': details,
            'id': id,
            'form': form,
        }
        return render(request, "home/comment.html", context)
    def post(self, request, *args,  **kwargs):
        print(request.POST)
        star = request.POST['rating']
        data = HireModel.objects.get(id=request.POST['id'])
        data.rating = star
        data.comment = request.POST['comment']
        # data.worker_status = True
        data.user_status = 1
        print(data)
        data.save()
        messages.success(request,"Service Completed Successfully") 
        return redirect('userservices')


@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:

            tables = Category.objects.all()
            jobs = jobmodel.objects.all()
            context = {
                'tables': tables,
                'current_path': "Categories",
                'data': jobs
            }
            return render(request, "home/category.html", context)
        else:
            return render(request, "home/page-403.html")


@method_decorator(login_required, name='dispatch')
class AddCategoryView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        context = {'form': form, 'current_path': "Add Category"}
        return render(request, "home/add_categoryform.html", context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
             try:
                data =Category.objects.create(
                    category_name = request.POST['category_name'],
                    image = request.FILES['image']
                    )
                data.save()
                messages.success(request, "Category added successfully")
                return redirect('category')
             except Exception as e : 
                print('error',e)
                messages.error(request, "error")
                return redirect( 'add_category')


@method_decorator(login_required, name='dispatch')
class DeleteCategoryView(View):
    def get(self, request, id):

        category_name = Category.objects.filter(id=id).values_list("category_name")[0][0]
        print(category_name)
        job_name = jobmodel.objects.filter(category=category_name).values_list("job_title")
        print(job_name,"jooooooooooooooooooob")
        jobs = jobmodel.objects.filter(category=category_name)
        jobs.delete()
        for i in job_name:
            print(i[0],"1111111")
            labours = labourmodels.objects.filter(job_title=i[0])
            labours.delete()
            print("Deleted.......................")
            print(labours,"user")
        print(jobs)

        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, "Category Deleted")
        return redirect('category')

@method_decorator(login_required, name='dispatch')
class Addjobsview(View):
    template = 'home/addjob.html'

    def get(self, request, *args, **kwargs):
        form = AddJobForm()
        context = {
            "form": form,
            'current_path': "Add Jobs"
        }
        # if not request.user.is_superuser:
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AddJobForm(request.POST)
            job_name = request.POST['job_name']
            category = request.POST['category']
            form.fields['category'].choices = [(category, category)]
            duplicate = jobmodel.objects.filter(job_title__icontains = job_name, category__icontains=category).exists()
            if duplicate:
                messages.error(request, "Job Already Exists")
                return redirect(reverse('category'))
            else:
                obj = jobmodel.objects.create(
                    job_title=job_name, category=category)
                messages.success(request, "Job Added Successfully")
                return redirect(reverse('category'))
        else:
            return render(request, self.template, {'form': form})

@method_decorator(login_required, name='dispatch')
class Deletejob(View):
    def get(self, request, id):
        job = jobmodel.objects.get(id=id)
        job.delete()
        messages.success(request, "Job Deleted")
        return redirect('category')


class Access_denied(View):
    template_name = ' home/page403.html  '

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class ManageUser(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:

            details = NewUserModel.objects.all().order_by('id').exclude(username='admin')
            context = {
                'details': details,
                'current_path': "Manage User",
            }
            return render(request, "home/manage-user.html", context)
        else:
            return render(request, "home/page-403.html")


@method_decorator(login_required, name='dispatch')
class UpdateUser(View):
    def get(self, request, id, *args, **kwargs):
        user = NewUserModel.objects.get(id=id)
        if user.is_active:
            user.is_active = False
            user.save()
            messages.success(request,"Inactivated Successfully")
        else:
            user.is_active = True
            user.save()
            messages.success(request,"Activated Successfully")
        return redirect('manageuser')

@method_decorator(login_required, name='dispatch')
class JobPostingView(View):
    template_name = 'home/job-posting.html'

    def get(self, request, id, *args, **kwargs):
        category = Category.objects.filter(
            id=id).values_list('category_name')[0][0]
        jobs = jobmodel.objects.filter(category=category).values()
        userjobs = JobPostingModel.objects.filter(hirer=request.user).values_list("job_title",flat=True)
        print(userjobs,"-----------------------")
        x =jobs.exclude(job_title__in=[userjobs])
        print(x,"--===--===--===----========")
        if not x:
            print("empty !!!!!!!!!!!!!!!!")
            messages.error(request,"No Remaining Jobs Found In This Category  !!!!")
            return redirect("labocategory2")
        else:
            
            form = JobPostingForm(initial=category, user=request.user.username,jobs=userjobs)
            context = {
                "form": form,
                "jobs": jobs,
                'current_path': "Apply Services"
            }
            return render(request, self.template_name, context)

    def post(self, request,id, *args, **kwargs):
        if request.method == 'POST':
            # applied = JobPostingModel.objects.filter
            
            form = JobPostingForm(request.POST)
            job = request.POST['job_title']
            userjobs = JobPostingModel.objects.filter(hirer=request.user).values_list("job_title",flat=True)
            if job in userjobs:
                messages.error(request,"Already Applied To This Job  !!")
                return redirect('labocategory2')
            else:
                obj = JobPostingModel.objects.create(
                    hirer=request.user.username,
                    place=request.POST['place'],
                    # image=request.FILES['image'],
                    job_title=request.POST['job_title'],
                    work_type=request.POST['work_type'],
                    phone=request.POST['phone'],
                    name=request.POST['name'])
                obj.save()
                messages.success(request,"Successfully Applied!!")
                return redirect('enlistedjobs')

 

        else:
            print("Method not allowed")
            return redirect('labocategory2')

@method_decorator(login_required, name='dispatch')
class ManageServices(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:

            details = labourmodels.objects.all().exclude(status=2).order_by('id')
            history = HireModel.objects.filter(status = 4).values()
            context = {
                'details': details,
                'history': history,
                'current_path': "Manage Services",
            }
            return render(request, "home/manage_services.html", context)
        else:
            return render(request, "home/page-403.html")

@method_decorator(login_required, name='dispatch')
class HireHistory(View):
    def get(self, request, *args, **kwargs):
        details = HireModel.objects.filter(
            Hire_name=request.user).filter(status__in=[4, 5]).order_by('id')
        context = {
            'details' : details,
            'current_path': "Laboshop History",
        }
        if details:
            return render(request, "home/hirehistory.html", context)
        else:
            messages.error(request,"Page is Empty")
            return render(request, "home/emptypage.html", context)


@method_decorator(login_required, name='dispatch')
class UpdateServices(View):
    def get(self, request, id, *args, **kwargs):
        status = labourmodels.objects.filter(id=id).values_list("status")[0][0]
        if status == 0:
            labourmodels.objects.filter(id=id).update(status=1)
            messages.success(request, "Activated Successfully !")
            return redirect("manageservices")
        elif status == 1:
            labourmodels.objects.filter(id=id).update(status=0)
            messages.success(request, "Inactivated Successfully!")
            return redirect("manageservices")
        else:
            labourmodels.objects.filter(id=id).update(status=0)
            messages.success(request, "Success !")
            return redirect("manageservices")


@method_decorator(login_required, name='dispatch')
class Labocategories2(View):
    template = 'home/labo-category2.html'

    def get(self, request, *args, **kwargs):
        data = Category.objects.all()
        job = jobmodel.objects.values_list('category', flat=True)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",job)
        context = {
            "data": data,
            "job": job,
            'current_path': "Provide Jobs",
            'MEDIA_ROOT':settings.NEW_VAR,

        }
        # total_work = JobPostingModel.objects.filter(Q(hirer=request.user.username) & Q(
        #     (Q(status=1) | Q(status=2) | Q(status=3)))).count()
        if data:
            total_work = JobPostingModel.objects.filter(Q(hirer=request.user.username) & Q(is_active = 1)).count()
            if total_work < 5:
                return render(request, self.template, context)
            else:
                messages.error(request, "Job Applying Limit Reached !!")
                return redirect("laboshop")
        else:
            return render(request,'home/emptypage.html',{'current_path':"Provide Jobs"})


@method_decorator(login_required, name='dispatch')
class ServiceRequests(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:

            details = labourmodels.objects.filter(status=2).order_by('id')
            context = {
                'details': details,
                'current_path':'Service Requests'
            }
            if details:
                return render(request, "home/service_requests.html", context)
            else:
                return render(request,'home/emptyKYC.html', context)

        else:
            return render(request,'home/page-403.html')

@method_decorator(login_required, name='dispatch')
class PendingKYC(View):
    template_name = 'home/pending-registration-requests.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:

            datas = NewUserModel.objects.filter(kyc_approved=0).order_by('id')
            context = {
                'media_url': settings.NEW_VAR,
                'datas': datas,
                'current_path': "Pending KYC  ",
            }
            if datas:
                return render(request, self.template_name, context)
            else:
                return render(request,'home/emptyKYC.html', context)
        else:
            return render(request,'home/page-403.html')

@method_decorator(login_required, name='dispatch')
class AcceptServices(View):
    def get(self, request, id, *args, **kwargs):
        status = labourmodels.objects.filter(id=id).values_list("status")[0][0]
        labourmodels.objects.filter(id=id).update(status=1)
        messages.success(request, "Request Accepted successfully !")
        return redirect("servicerequests")

@method_decorator(login_required, name='dispatch')
class RejectServices(View):
    def get(self, request, id):
        data = labourmodels.objects.get(id=id)
        data.delete()
        messages.success(request, "Request Rejected Successfully")
        return redirect('servicerequests')

@method_decorator(login_required, name='dispatch')
class JobRequests(View):
    template_name = 'home/jobrequests.html'
    def get(self, request, *args, **kwargs):
        hire = HireModel.objects.filter(status=3,Hire_name=request.user)
        print(hire,"hiiiiiiiiiiiiiiii")
        if hire!= None:
            # requests = AppliedJobs.objects.filter(hirer=request.user.username).exclude(status=3)
            requests = AppliedJobs.objects.filter(Q(hirer=request.user.username)&Q(status=0))
            for data in requests:
                for hirer in hire:
                    print(data.worker_uname,hirer.worker_name,"whatttttttttttttttttttttttttttttt")
                    if data.worker_uname == hirer.worker_name:
                        requests = requests.exclude(worker_uname=data.worker_uname)
                        print(requests,"reqqqqqqqqqqqqqqqqqqqq")
        print(requests,"--------------------------")
        # requetn = HireModel.objects.filter(status=3)


        
        context = {
            'requests': requests,
            'current_path': "Job requests",
            }
        if requests:
            return render(request, 'home/jobrequests.html', context)
        else:
            return render(request,'home/emptyservices.html',{'current_path':"Job requests"})
        


@method_decorator(login_required, name='dispatch')
class CancelJobRequests(View):
    def get(self, request,id, *args, **kwargs):
        id = id
        cancel = AppliedJobs.objects.filter(id=id).update(status=3)
        messages.success(request, " Request Cancelled")
        return redirect('jobrequests')


@method_decorator(login_required, name='dispatch')
class ApproveUser(View):
    def get(self, request,  id):
        try:
            user = NewUserModel.objects.get(id=id)
            user.kyc_approved = True
            user.save()
            messages.success(request, "Approved User successfully")
            return redirect('pendingkyc')
        except Exception as e:
            messages.error(request, "An error occured during the approval.")

@method_decorator(login_required, name='dispatch')
class RejectUser(View):
    def get(self, request, id):
        user = NewUserModel.objects.get(id=id)
        user.delete()
        messages.success(request, "Rejected User successfully")
        return redirect('pendingkyc')

@method_decorator(login_required, name='dispatch')
class JobRequestUpdate(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        req = AppliedJobs.objects.filter(id=id).values()
        job = AppliedJobs.objects.filter(id=id).values_list("job_title")[0][0]
        req.update(status=1)
        reject = AppliedJobs.objects.filter(job_title = job).exclude(status=1)
        reject.update(status=2)
        messages.success(request, "Updated successfully")
        return redirect('jobrequests')


@method_decorator(login_required, name='dispatch')
class ProvidedJobs(View):
    template_name = "home/provided-jobs-list.html"
    def get(self, request, *args, **kwargs):
        jobs = JobPostingModel.objects.filter(
            hirer=request.user.username)
        context = {'jobs': jobs,
                    'current_path': "Enlisted Jobs"}
        if jobs:
            return render(request,self.template_name , context)
        else:
            messages.error(request, "No Services Found")
            return render(request,"home/emptyservices.html",context)
@method_decorator(login_required, name='dispatch')
class LookForJobs(View):
    def get(self, request, *args, **kwargs):
        
        appliedones = AppliedJobs.objects.filter(worker_uname=request.user.username)
        filter=request.GET.get('filter')
        job_title = jobmodel.objects.filter(id=filter)
        datajob = jobmodel.objects.all()
        if request.GET.get('filter') is not None and request.GET.get('filter') != '':
            jobs = JobPostingModel.objects.filter(Q(is_active=1)&Q(job_title=job_title)).exclude(hirer=request.user.username).values()
            # data = labourmodels.objects.filter(Q(job_title=job)&Q(status=1)).exclude(username=request.user.username)		
        else:
            jobs = JobPostingModel.objects.filter(is_active=1).exclude(hirer=request.user.username).values()
            # data = labourmodels.objects.filter(status=1).exclude(username=request.user.username)
        datacategory=Category.objects.values()
        context = {
            'media_url': settings.NEW_VAR,

            'jobs': jobs,
            'current_path': "Available Jobs",
            'datacategory':datacategory,
            "datajob":datajob,
        }
        if request.user.is_sub:
            if jobs:
                return render(request, "home/lookforjobs.html", context)
            else:
                return render(request,"home/emptyworkerpage.html",context)
        else:
            messages.error(request,"Subscription required !! ")
            return redirect("workerview")

@method_decorator(login_required, name='dispatch')
class LookJobs(View):
    def get(self, request, *args, **kwargs):
        data = AppliedJobs.objects.filter(worker_uname=request.user).values()
        context = {
            'media_url': settings.NEW_VAR,
            'data': data,
            'current_path': "Applied Jobs"  
        }
        if request.user.is_sub:
            if data:
                return render(request, "home/appliedjobs.html", context)
            else:
                return render(request,"home/emptyworkerpage.html",context)
        else:
            messages.error(request,"Subscription required !! ")
            return redirect("workerview")
@method_decorator(login_required, name='dispatch')
class CancelLookJobs(View):
    def get(self, request,id, *args, **kwargs):
        delete = AppliedJobs.objects.filter(id=id)
        delete.delete()
        messages.success(request,"Deleted Successfully")
        return redirect('lookjobs')
@method_decorator(login_required, name='dispatch')
class EditLookJobs(View):
    def get(self, request,id, *args, **kwargs):
        # delete = AppliedJobs.objects.filter(id=id)
        # delete.delete()
        data=AppliedJobs.objects.filter(id=id).first()
        context={
            "id":id,
            "location":data.place,
            "rate":data.rate,


        }
        template= 'home/editlookforjob.html'

        return render(request,template,context)
    def post(self, request, *args, **kwargs):
        id=request.POST.get("id")
        work_mode=request.POST.get("work_mode")
        location=request.POST.get("location")
        rate=request.POST.get("rate")
        AppliedJobs.objects.filter(id=id).update(work_type=work_mode,place=location,rate=rate)
        messages.success(request, "Updated successfully")
        return redirect('lookjobs')


@method_decorator(login_required, name='dispatch')
class  UpdateEnlistedJobStatus(View):
    def get(self, request,id, *args, **kwargs):
        job = JobPostingModel.objects.get(id=id)
        print(job.is_active,"activityyyyyyyyyyyyyyyyyyyyyyyyy")
        if job.is_active:
            job.is_active = False
            job.save()
            messages.success(request,"Inactivated Successfully! ")
        else:
            job.is_active = True
            job.save()
        messages.success(request," Activated Successfully! ")
        return redirect('enlistedjobs')
@method_decorator(login_required, name='dispatch')
class  deleteenlisted(View):
    def get(self, request,id, *args, **kwargs):
        job = JobPostingModel.objects.get(id=id)
        job.delete()
        messages.success(request,"Successfully Deleted! ")
        return redirect('enlistedjobs')

@method_decorator(login_required, name='dispatch')
class JobRequestPay(View):
    template = 'home/jobreqpay.html'
    def get(self, request, id, *args, **kwargs):
        rate = AppliedJobs.objects.filter(id=id).values_list("rate")[0][0]
        context={
            "rate":rate,
            "id":id,
        }
        return render(request,self.template,context)

@method_decorator(login_required, name='dispatch')
class confirmpaymentjob(View):
    def get(self ,request,id, *arg, **kwargs):
        wallet_bal = NewUserModel.objects.filter(username=request.user).values_list("wallet")[0][0]
        rate = AppliedJobs.objects.filter(id=id).values_list("rate")[0][0]
        if wallet_bal >= rate:
            NewUserModel.objects.filter(username=request.user).update(wallet=wallet_bal-rate)
            messages.success(request,"Success !!!!")
            return redirect('jobrequestupdate',id)
        else:
            messages.error(request,"Not enough balance !!!")
            return redirect('confirmpaymentjob',id)



@method_decorator(login_required, name='dispatch')
class ConfirmOTP(View):
    def get(self ,request,id, *arg, **kwargs):
        return render(request, "home/otp.html",{"id":id})   
    def post(self,request,*arg,**kwargs):
        id = request.POST['id']   
        n1 = request.POST['first']   
        n2 = request.POST['second']   
        n3 = request.POST['third']   
        n4 = request.POST['fourth']   
        n5 = request.POST['fifth']   
        n6 = request.POST['sixth']
        # print(id,"------",n1,"------",n2,"------",n3,"------",n4,"------",n5,"------",n6)
        # a=[]
        a= n1+n2+n3+n4+n5+n6
        print(a,"--==========--")
        otp = HireModel.objects.filter(id=id).values_list("otp")[0][0]
        print(otp,"oooooooooooooooootttttttttppppppp")
        if otp==int(a):
            print("accepted......")
            return redirect("completedservices",id)

        else:
            messages.error(request,"OTP is not valid !!")
            print("rejected......")
            return redirect("confirmotp",id)

@method_decorator(login_required, name='dispatch')
class AdminDashboard(View):
    def get(self, request,*args, **kwargs):
        if request.user.is_superuser:
            shopPurchase = PurchaseModel.objects.filter(status=3).aggregate(Sum('Total'))
            packageRevenue = PurchaseModel.objects.filter(status=0).aggregate(Sum('Total'))
            totalMembers = NewUserModel.objects.filter(kyc_approved=1).exclude(is_superuser=1).count()
            activeServices = labourmodels.objects.filter(status=1).count()
            activeVacancies = JobPostingModel.objects.filter(status=1).count()
            context ={
			    'shopPurchase': shopPurchase["Total__sum"],
			    'packageRevenue': packageRevenue["Total__sum"],
			    'activeVacancies': activeVacancies,
			    'activeServices': activeServices,
			    'totalMembers': totalMembers,
                "current_path":''
                }

            return render(request,'home/admindashboard.html',context)
        else:
            return render(request,'home/page-403.html',{})



class SearchCityView(View):

    def get (self, request,*args, **kwargs):

        return HttpResponse("Method Not Allowed")

    def post(self, request, *args, **kwargs):

        feildname = kwargs.pop('feildname')
        print("pooee",feildname)
        search_text = request.POST.get(feildname)

        print("#########################INSIDE SearchCityView" ,search_text ,"##################")

        if search_text:

            if len(search_text)>=3:

                results=CitiesModel.objects.filter(name__icontains=search_text)

                print(results,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

                return render(request, 'search/cities-list.html',{"results":results})

            else:

                return render(request, 'search/cities-list.html',{})

        else:

        # return render(request, 'search/cities-list.html',{"results":results})

            return render(request, 'search/cities-list.html',{})            



class Reported(View):
    def get(self, request):
        report= ReeportModel.objects.all()
        if request.user.is_superuser:
            return render(request, 'home/reported.html',{"current_path":"Reported Issues","report":report,})
        else:
            return render(request, 'home/page-403.html')