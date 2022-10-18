from django.urls import path
from . import views
urlpatterns = [
	path("user/",views.Home.as_view(),name="home"),
	path("shop/",views.Shop.as_view(),name="shop"),
	path("laboshop/",views.Shop.as_view(),name="laboshop"),

]
