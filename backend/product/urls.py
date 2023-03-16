from django.urls import path

from . import views


urlpatterns = [
    path('', views.product_alt_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/destroy/', views.product_destroy_view),
    path('<int:pk>/', views.product_alt_view)
]