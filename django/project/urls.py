
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path('',include('ecommerce.urls'),name='home'),
    path('',include('apps.home.urls'),name='home'),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    # path("", include("apps.home.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)