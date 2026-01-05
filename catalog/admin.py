from django.contrib import admin
from .models import Category, Product, TechnicalSpecification, Service, ServiceRequest

class TechnicalSpecificationInline(admin.TabularInline):
    model = TechnicalSpecification
    extra = 2

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [TechnicalSpecificationInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'slug') # نمایش آیکون انتخابی در لیست
    prepopulated_fields = {'slug': ('title',)} # ساخت خودکار اسلاگ از روی عنوان

admin.site.register(Category)
admin.site.register(ServiceRequest)

