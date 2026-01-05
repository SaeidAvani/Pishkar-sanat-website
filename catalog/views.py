from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Service, ServiceRequest

def home_view(request):
    products = Product.objects.filter(is_active=True)[:6]
    services = Service.objects.all() # خواندن خدمات از دیتابیس
    return render(request, 'catalog/home.html', {'products': products, 'services': services})

def faq_view(request):
    return render(request, 'catalog/faq.html')

def blog_cng_maintenance_view(request):
    return render(request, 'catalog/blog_cng_maintenance.html')

def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'catalog/service_detail.html', {'service': service})

def service_request_view(request):
    if request.method == 'POST':
        ServiceRequest.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            company_name=request.POST.get('company'),
            service_type=request.POST.get('service_type'),
            message=request.POST.get('message')
        )
        messages.success(request, 'درخواست شما ثبت شد. به زودی تماس می‌گیریم.')
        return redirect('service_request')
    return render(request, 'catalog/service_request.html')

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
