from django.urls import path
from . import views
from .views import Deleteproduct
from .views import UpdateProduct

urlpatterns = [
	path("user/",views.Home.as_view(),name="home"),
	path("shop/",views.Shop.as_view(),name="shop"),
	path("laboshopcategory/",views.LaboShopCategory.as_view(),name="laboshopcategory"),
	path("laboshop/",views.LaboShop.as_view(),name="laboshop"),
	path("addstock/",views.Addproduct.as_view(),name="addproduct"),
	path("stocklist/",views.ProductTable.as_view(),name="stocklist"),
	path("laboregister/<str:id>",views.LaboRegister.as_view(), name="laboregister"),
	path("labocategory/",views.Labocategories.as_view(), name="labocategory"),
	path("cart",views.CartView.as_view(),name="cart"),
	path("addtocart/<str:id>",views.AddtocartView.as_view(),name="addtocart"),
	path('del_from_cart/<int:id>/', views.DelFromCartView.as_view(), name="del_from_cart"),
	path("checkout/",views.CheckoutView.as_view(),name="checkout"),
	path('delete_product/<int:id>/', views.Deleteproduct.as_view(), name="delete_product"),
	path('updateProduct/<int:id>/', UpdateProduct.as_view(), name="updateProduct"),
	path("hire_now/<int:id>/",views.HireNowView.as_view(),name="hire_now"),
	path("hirenowpayments/<int:id>/",views.HireNowPayments.as_view(),name="hirenowpayments"),
	path('cancel_request/<int:id>/', views.CancelRequest.as_view(), name="cancel_request"),
	path("active_service/",views.ActiveServices.as_view(),name="active_service"),
	path('increase_no/', views.IncreaseNo.as_view(), name="increase-no"),
	path('decrease_no/', views.DecreaseNo.as_view(), name="decrease-no"),
	path('assigned/', views.Assignedworks.as_view(), name="assigned"),
	path('invoice/', views.Invoice.as_view(), name="invoice"),
	path('accept/<int:id>', views.Acceptservice.as_view(), name="acceptservice"),
	path('togglestatus/<int:id>', views.Togglestatus.as_view(), name="togglestatus"),
	path('subscribe/<int:id>', views.Subscribe.as_view(), name="subscribe"),
	path('',views.HomePage.as_view(), name="homepage"),
	path('payment/<int:id>',views.Payment.as_view(), name="payment"),
	path('confirmpayment/<int:id>',views.ConfirmPay.as_view(), name="confirmpayment"),
	path('packages/',views.Packages.as_view(), name="packages"),
	path('delete_package/<int:id>/', views.Deletepackage.as_view(), name="delete_package"),
	path('updatePackage/<int:id>/', views.UpdatePackage.as_view(), name="updatePackage"),
	path("addpackage/",views.Addpackage.as_view(),name="addpackage"),
	path("membership/",views.membership.as_view(), name="membership"),
	path("workerview/",views.Workerview.as_view(), name="workerview"),
	path("userprofile/",views.Individual.as_view(), name="userprofile"),
	path('userpayments/<int:id>/',views.Userpayments.as_view(), name="userpayments"),
	path('refundhistory/',views.RefundHistoryUser.as_view(), name="refundhistory"),
	path('refundhistoryworker/',views.RefundHistoryWorker.as_view(), name="refundhistoryworker"),
	path('labotransactions/',views.LaboTransactions.as_view(), name="labotransactions"),
	path('products_history/',views.producthistory.as_view(), name="products_history"),
	path('search_products/',views.SearchProducts.as_view(), name="search_products"),
	path('packagehistory/',views.PurchaseHistory.as_view(), name="packagehistory"),
	path('adminhirehistory/',views.AdminHireHistory.as_view(), name="adminhirehistory"),
	path('refundhistory/',views.RefundHistoryView.as_view(), name="refundhistory"),



]

