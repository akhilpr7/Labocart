
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('',include('ecommerce.urls'),name='home'),
    path('',include('apps.home.urls'),name='home'),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    # path("", include("apps.home.urls"))
]