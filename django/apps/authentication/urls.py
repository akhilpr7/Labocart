from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginViews.as_view(), name="login"),
    path('register/', views.RegisterViews.as_view(), name="register"),
]
