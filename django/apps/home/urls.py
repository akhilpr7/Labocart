from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.HomeView.as_view(), name="dashboard"),
    path('transactions/', views.TransacView.as_view(), name="transaction"),
    path('funds/', views.FundView.as_view(), name="funds"),
    path('requested', views.ServiceView.as_view(), name="requested"),
    path('logout/', views.HomeView.as_view(), name="logout"),

]
