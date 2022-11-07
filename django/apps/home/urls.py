from django.urls import path, include
from . import views

urlpatterns = [

    path('dashboard/', views.HomeView.as_view(), name="dashboard"),
    path('transactions/', views.TransactionView.as_view(), name="transaction"),
    path('funds/', views.FundView.as_view(), name="funds"),
    path('access_denied/', views.Access_denied.as_view(), name="access_denied"),
    path('requested/', views.ServiceView.as_view(), name="requested"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('logout/', views.HomeView.as_view(), name="logout"),
    path('add_category/', views.AddCategoryView.as_view(), name="add_category"),
    path('delete_category/<int:id>/', views.DeleteCategoryView.as_view(), name="delete_category"),
    path('add_jobs/', views.Addjobsview.as_view(), name="add_jobs"),
    path('delete_job/<int:id>/', views.Deletejob.as_view(), name="delete_job"),
    path('userservices/', views.Userservices.as_view(),name="userservices"),
    path('jobrequests/', views.JobRequests.as_view(),name="jobrequests"),
    path('jobrequestupdate/<int:id>/', views.JobRequestUpdate.as_view(),name="jobrequestupdate"),
    path('workerservices/', views.Workerservices.as_view(),name="workerservices"),
    path('lookforjobs/', views.LookForJobs.as_view(),name="lookforjobs"),
    path('completedservices/<int:id>/', views.CompletedService.as_view(), name="completedservices"),
    path('usercompletedservices/<int:id>/', views.UserCompletedService.as_view(), name="usercompletedservices"),
    path('rating/<int:id>', views.RatingView.as_view(),name="rating"),
    path('ratings/<int:id>/<int:id1>/', views.Ratings.as_view(),name="ratings"),
    path('manageuser/', views.ManageUser.as_view(), name="manageuser"),
    path('updateuser/<int:id>/', views.UpdateUser.as_view(),name="updateuser"),
    path('jobpost',views.JobPostingView.as_view(),name="job-posting"),
    path('applyform/<int:id>/',views.ApplyFormView.as_view(),name="applyform"),
    path('manageservices/', views.ManageServices.as_view(), name="manageservices"),
    path('updateservices/<int:id>/', views.UpdateServices.as_view(),name="updateservices"),
    path('jobpost/<str:id>',views.JobPostingView.as_view(),name="job-posting"),
	path("labocategory2/",views.Labocategories2.as_view(), name="labocategory2"),
    path("servicerequests",views.ServiceRequests.as_view(),name="servicerequests"),
    path('acceptservices/<int:id>/', views.AcceptServices.as_view(), name="acceptservices"),
    path('rejectservices/<int:id>/', views.RejectServices.as_view(), name="rejectservices"),
    path("pendingkyc",views.PendingKYC.as_view(),name="pendingkyc"),
    path("approveuser/<int:id>",views.ApproveUser.as_view(),name="approveuser"),
    


]
