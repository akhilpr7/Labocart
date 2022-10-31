from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
# from ecommerce.views import LaboRegister
urlpatterns = [
    path('login/', views.LoginViews.as_view(redirect_authenticated_user=True), name="login"),
    path('register/', views.RegisterViews.as_view(), name="register"),
    path('Demo/', views.Demo.as_view(), name="Demo"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('update_profile/', views.UpdateProfileView.as_view(), name="update_profile"),
   
    


]
