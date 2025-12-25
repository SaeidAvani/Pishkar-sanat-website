from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'), # این خط اضافه شد
    path('services/', views.service_list, name='service_list'), 
]