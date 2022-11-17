from multiprocessing import context
from tempfile import template
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ecommerce.models import HireModel, PurchaseModel,RequestsModel,RefundHistory,PackageModel
from .forms import AddJobForm, CategoryForm, JobPostingForm, AddFundForm, ApplyForm,CommentForm
from .models import Category, JobPostingModel, AppliedJobs,Category
from django.contrib import messages
from django.urls import reverse
from authentication.models import jobmodel, NewUserModel, labourmodels
from django.views.generic import ListView
from django.db.models import Q
import pdb
import datetime
from django.views.decorators.cache import cache_control

# Create your views here.


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):

        req_count = HireModel.objects.filter(Q(Hire_name=request.user)&(Q(status=4)|Q(status=5))).count()
        purchase = PurchaseModel.objects.filter(username=request.user).values_list("Total")
        print(request.user.package,"packaaaaaaaa")
        print(request.user.subscribed_at,"packaaaaaaaa")
        sub_at=request.user.subscribed_at
        a = datetime.datetime.now().date()
        print(a,"current time issssss")
         
        if sub_at != None:
            diff = a-sub_at
            print(diff.days,"differenceeeeeeeeeeee")
            validity = PackageModel.objects.filter(id=request.user.package).values_list("validity")[0][0]

            tot_purchase = 0
            for i in purchase:
                tot_purchase += i[0]

            context ={
                "req" : req_count,
                "tot" : tot_purchase,
                "exp" : validity-diff.days, 
            }
        else:
            tot_purchase = 0
            for i in purchase:
                tot_purchase += i[0]
            context ={
                "req" : req_count,
                "tot" : tot_purchase,
                
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
                return redirect(reverse('dashboard'))
            else:
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
                    return render(request, "home/emptylaboshop.html",context)
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
            return render(request, "home/emptylaboshop.html",context)

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
            return render(request, "home/emptylookforjobs.html",context)

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
                form = ApplyForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Success")
                    return redirect('lookforjobs')
                else:
                    messages.error(request, "error")
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
            return render(request, "home/emptylaboshop.html", context)
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
        return redirect('userservices')


@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, *args, **kwargs):
        tables = Category.objects.all()
        jobs = jobmodel.objects.all()
        context = {
            'tables': tables,
            'current_path': "Categories",
            'data': jobs
        }
        return render(request, "home/category.html", context)


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
            obj = jobmodel.objects.create(
                job_title=job_name, category=category)
            return redirect(reverse('category'))
        else:
            return render(request, self.template, {'form': form})
        # else:
        #     return render(request, self.template, {'form': form})

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
        details = NewUserModel.objects.all().order_by('id').exclude(username='admin')
        context = {
            'details': details,
            'current_path': "Manage User",
        }
        return render(request, "home/manage-user.html", context)

@method_decorator(login_required, name='dispatch')
class UpdateUser(View):
    def get(self, request, id, *args, **kwargs):
        user = NewUserModel.objects.get(id=id)
        if user.is_active:
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()
        return redirect('manageuser')

@method_decorator(login_required, name='dispatch')
class JobPostingView(View):
    template_name = 'home/job-posting.html'

    def get(self, request, id, *args, **kwargs):
        category = Category.objects.filter(
            id=id).values_list('category_name')[0][0]
        jobs = jobmodel.objects.filter(category=category).values()
        form = JobPostingForm(initial=category, user=request.user.username)
        context = {
            "form": form,
            "jobs": jobs,
            'current_path': "Apply Services"
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # applied = JobPostingModel.objects.filter
            form = JobPostingForm(request.POST,request.FILES)
            try:
                obj = JobPostingModel.objects.create(
                    hirer=request.user.username,
                    place=request.POST['place'],
                    image=request.FILES['image'],
                    job_title=request.POST['job_title'],
                    work_type=request.POST['work_type'],
                    phone=request.POST['phone'],
                    name=request.POST['name'])
                obj.save()
                return redirect('enlistedjobs')

            except Exception :
                print(Exception)
                return redirect('labocategory2')

        else:
            print("not valid")
            return redirect('labocategory')

@method_decorator(login_required, name='dispatch')
class ManageServices(View):
    def get(self, request, *args, **kwargs):
        details = labourmodels.objects.all().exclude(status=2).order_by('id')
        history = HireModel.objects.filter(status = 4).values()
        context = {
            'details': details,
            'history': history,
            'current_path': "Manage Services",
        }
        return render(request, "home/manage_services.html", context)

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
            return render(request, "home/emptylaboshop.html", context)


@method_decorator(login_required, name='dispatch')
class UpdateServices(View):
    def get(self, request, id, *args, **kwargs):
        status = labourmodels.objects.filter(id=id).values_list("status")[0][0]
        if status == 0:
            labourmodels.objects.filter(id=id).update(status=1)
            messages.success(request, "Success !")
            return redirect("manageservices")
        elif status == 1:
            labourmodels.objects.filter(id=id).update(status=0)
            messages.success(request, "Success !")
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
        context = {
            "data": data,
            'current_path': "Provide Jobs",
            'MEDIA_ROOT':settings.NEW_VAR,

        }
        # total_work = JobPostingModel.objects.filter(Q(hirer=request.user.username) & Q(
        #     (Q(status=1) | Q(status=2) | Q(status=3)))).count()
        total_work = JobPostingModel.objects.filter(Q(hirer=request.user.username) & Q(status = 0)).count()
        if total_work < 5:
            return render(request, self.template, context)
        else:
            messages.error(request, "Job Applying Limit Reached !!")
            return redirect("laboshop")


@method_decorator(login_required, name='dispatch')
class ServiceRequests(View):
    def get(self, request, *args, **kwargs):
        details = labourmodels.objects.filter(status=2).order_by('id')
        context = {
            'details': details,
            'current_path':'Service Requests'
        }
        if details:
            return render(request, "home/service_requests.html", context)
        else:
            return render(request,'home/emptyservicerequests.html', context)



@method_decorator(login_required, name='dispatch')
class PendingKYC(View):
    template_name = 'home/pending-registration-requests.html'

    def get(self, request, *args, **kwargs):
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


@method_decorator(login_required, name='dispatch')
class AcceptServices(View):
    def get(self, request, id, *args, **kwargs):
        status = labourmodels.objects.filter(id=id).values_list("status")[0][0]
        labourmodels.objects.filter(id=id).update(status=1)
        messages.success(request, "Success !")
        return redirect("servicerequests")

@method_decorator(login_required, name='dispatch')
class RejectServices(View):
    def get(self, request, id):
        data = labourmodels.objects.get(id=id)
        data.delete()
        messages.success(request, "Cancelled")
        return redirect('servicerequests')

@method_decorator(login_required, name='dispatch')
class JobRequests(View):
    template_name = 'home/jobrequests.html'
    def get(self, request, *args, **kwargs):
        hire = HireModel.objects.filter(status=3)
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
        
        return render(request, "home/jobrequests.html", context)


@method_decorator(login_required, name='dispatch')
class CancelJobRequests(View):
    def get(self, request,id, *args, **kwargs):
        id = id
        cancel = AppliedJobs.objects.filter(id=id).update(status=3)
        return redirect('jobrequests')


@method_decorator(login_required, name='dispatch')
class ApproveUser(View):
    def get(self, request,  id):
        try:
            user = NewUserModel.objects.get(id=id)
            user.kyc_approved = True
            user.save()
            messages.success(request, "Approved User.")
            return redirect('pendingkyc')
        except Exception as e:
            messages.error(request, "An error occured during the approval.")

@method_decorator(login_required, name='dispatch')
class RejectUser(View):
    def get(self, request, id):
        user = NewUserModel.objects.get(id=id)
        user.delete()
        messages.success(request, "Rejected User")
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
            return render(request,"home/emptylaboshop.html",context)
@method_decorator(login_required, name='dispatch')
class LookForJobs(View):
    def get(self, request, *args, **kwargs):
        jobs = JobPostingModel.objects.filter(is_active=1).exclude(hirer=request.user.username).values()
        appliedones = AppliedJobs.objects.filter(worker_uname=request.user.username)


        context = {
            'media_url': settings.NEW_VAR,

            'jobs': jobs,
            'current_path': "Available Jobs"
        }
        if request.user.is_sub:
            if jobs:
                return render(request, "home/lookforjobs.html", context)
            else:
                return render(request,"home/emptylookforjobs.html",context)
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
                return render(request,"home/emptylookforjobs.html",context)
        else:
            messages.error(request,"Subscription required !! ")
            return redirect("workerview")
@method_decorator(login_required, name='dispatch')
class CancelLookJobs(View):
    def get(self, request,id, *args, **kwargs):
        delete = AppliedJobs.objects.filter(id=id)
        delete.delete()
        return redirect('lookjobs')


@method_decorator(login_required, name='dispatch')
class  UpdateEnlistedJobStatus(View):
    def get(self, request,id, *args, **kwargs):
        job = JobPostingModel.objects.get(id=id)
        if job.is_active:
            job.is_active = False
            job.save()
        else:
            job.is_active = True
            job.save()
        messages.success(request,"Success! ")
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


