from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),  
]