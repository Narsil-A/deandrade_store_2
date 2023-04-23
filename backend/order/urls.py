from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from order import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('checkout/', views.checkout),
    path('', views.order_list_view),  
]