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
    path('canceljobrequests/<int:id>', views.CancelJobRequests.as_view(),name="canceljobrequests"),
    path('jobrequestupdate/<int:id>/', views.JobRequestUpdate.as_view(),name="jobrequestupdate"),
    path('workerservices/', views.Workerservices.as_view(),name="workerservices"),
    path('lookforjobs/', views.LookForJobs.as_view(),name="lookforjobs"),
    path('lookjobs/', views.LookJobs.as_view(),name="lookjobs"),
    path('cancelLook/<int:id>/', views.CancelLookJobs.as_view(),name="cancelLook"),
    path('editlook/<int:id>/', views.EditLookJobs.as_view(),name="editlook"),
    path('completedservices/<int:id>/', views.CompletedService.as_view(), name="completedservices"),
    path('uncompletedservices/<int:id>/', views.UnCompletedService.as_view(), name="uncompletedservices"),
    path('usercompletedservices/<int:id>/', views.UserCompletedService.as_view(), name="usercompletedservices"),
    path('rating/<int:id>', views.RatingView.as_view(),name="rating"),
    path('manageuser/', views.ManageUser.as_view(), name="manageuser"),
    path('updateuser/<int:id>/', views.UpdateUser.as_view(),name="updateuser"),
    path('jobpost',views.JobPostingView.as_view(),name="job-posting"),
    path('applyform/<int:id>/',views.ApplyFormView.as_view(),name="applyform"),
    path('manageservices/', views.ManageServices.as_view(), name="manageservices"),
    path('hirehistory/', views.HireHistory.as_view(), name="hirehistory"),
    path('updateservices/<int:id>/', views.UpdateServices.as_view(),name="updateservices"),
    path('jobpost/<str:id>',views.JobPostingView.as_view(),name="job-posting"),
	path("labocategory2/",views.Labocategories2.as_view(), name="labocategory2"),
    path("servicerequests/",views.ServiceRequests.as_view(),name="servicerequests"),
    path('acceptservices/<int:id>/', views.AcceptServices.as_view(), name="acceptservices"),
    path('rejectservices/<int:id>/', views.RejectServices.as_view(), name="rejectservices"),
    path("pendingkyc",views.PendingKYC.as_view(),name="pendingkyc"),
    path("approveuser/<int:id>",views.ApproveUser.as_view(),name="approveuser"),
    path("rejectuser/<int:id>",views.RejectUser.as_view(),name="rejectuser"),
    path('enlistedjobs/', views.ProvidedJobs.as_view(),name="enlistedjobs"),
    path('enlistedjobstatus/<int:id>/', views.UpdateEnlistedJobStatus.as_view(),name="enlistedjobstatus"),
    path('jobrequestpay/<int:id>',views.JobRequestPay.as_view(),name='jobrequestpay'),
    path('confirmpaymentjob/<int:id>',views.confirmpaymentjob.as_view(),name='confirmpaymentjob'),
    path('deleteenlisted/<int:id>/',views.deleteenlisted.as_view(),name='deleteenlisted'),
    path('confirmotp/<int:id>/',views.ConfirmOTP.as_view(),name='confirmotp'),
    path('admindashboard',views.AdminDashboard.as_view(),name='admindashboard'),
    path('search_city/<str:feildname>',views.SearchCityView.as_view(),name='search-city'),
    path('issues/',views.Reported.as_view(),name='issues'),
    path('delivery/<int:id>/',views.Delivery.as_view(),name='delivery'),
    path('deliverd/<int:id>/',views.Deliverd.as_view(),name='deliverd'),
    path('cancel-order/<int:id>/',views.OrderCancelView.as_view(),name='cancel-order'),
    path('confirmproductotp/<int:id>/',views.ConfirmProductOtp.as_view(),name='confirmproductotp'),
    path('refundworkerfull/<int:id>/',views.RefundWorkerFull.as_view(),name='refundworkerfull'),
    path('refundhirerfull/<int:id>/',views.RefundHirerFull.as_view(),name='refundhirerfull'),
    path('refundsplit/<int:id>/',views.RefundSplit.as_view(),name='refundsplit'),
    path('deleteissue/<int:id>/',views.DeleteIssue.as_view(),name='deleteissue'),


]
