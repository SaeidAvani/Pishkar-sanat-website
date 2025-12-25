from django.contrib import admin
from .models import Category, Product, Service, Client, ServiceRequest

# تنظیمات هدر پنل مدیریت (برای اینکه نام شرکت را ببینی)
admin.site.site_header = "مدیریت سایت دادفر صنعت"
admin.site.site_title = "پنل مدیریت دادفر صنعت"
admin.site.index_title = "به پنل مدیریت خوش آمدید"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # این خط باعث می‌شود وقتی نام را تایپ می‌کنی، آدرس سئو (Slug) خودکار پر شود
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'model_type', 'is_active', 'created_at')
    list_filter = ('category', 'model_type', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active',) # امکان فعال/غیرفعال کردن سریع از لیست

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_on_home')
    list_editable = ('show_on_home',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type')
    search_fields = ('full_name', 'phone', 'machine_model')
    list_editable = ('status',) # تغییر وضعیت درخواست بدون باز کردن صفحه