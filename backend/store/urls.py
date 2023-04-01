from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')) # this will run in the localhost:8000/store/
]
# path of the store api: localhost:8000/store/