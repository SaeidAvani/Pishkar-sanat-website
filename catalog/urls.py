from django.urls import path
from .views import home_view, product_detail_view, service_request_view, service_detail_view, faq_view, blog_cng_maintenance_view

urlpatterns = [
    path('', home_view, name='home'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('service/<str:slug>/', service_detail_view, name='service_detail'),
    path('request-service/', service_request_view, name='service_request'),
    path('faq/', faq_view, name='faq'),
    path('blog/cng-compressor-maintenance/', blog_cng_maintenance_view, name='blog_cng_maintenance'),
]
