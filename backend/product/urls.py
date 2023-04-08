from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('auth/', obtain_auth_token), # creating an endpoint to generate the auth
    path('', views.product_list_create_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/destroy/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail')
]