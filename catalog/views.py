from django.shortcuts import render
from .models import Product, Service, Client, Category
from django.shortcuts import render, get_object_or_404 # این خط اول فایل باشد

def home(request):
    # دریافت اطلاعات از دیتابیس
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:6] # ۶ محصول آخر
    services = Service.objects.filter(is_active=True)
    clients = Client.objects.filter(show_on_home=True)
    
    context = {
        'products': products,
        'services': services,
        'clients': clients,
    }
    return render(request, 'catalog/home.html', context)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
def service_list(request):
    # تمام سرویس‌هایی که فعال هستند را از دیتابیس بگیر
    services = Service.objects.filter(is_active=True)
    
    # آن‌ها را برای نمایش به قالب بفرست
    context = {
        'services': services
    }
    return render(request, 'catalog/service_list.html', context)