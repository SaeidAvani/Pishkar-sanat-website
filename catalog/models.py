from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
import os

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="آدرس سئو")
    
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name

class Product(models.Model):
    MODEL_TYPE_CHOICES = [
        ('compressor', 'کمپرسور'),
        ('oxygen_generator', 'ژنراتور اکسیژن'),
        ('spare_parts', 'قطعات یدکی'),
        ('oil', 'روغن صنعتی'),
        ('cng', 'تجهیزات CNG'),
        ('other', 'سایر'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="دسته‌بندی")
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات فنی")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر محصول")
    model_type = models.CharField(
        max_length=50,
        choices=MODEL_TYPE_CHOICES,
        default='other',
        verbose_name="نوع محصول"
    )
    is_active = models.BooleanField(default=True, verbose_name="نمایش در سایت")

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.mode != 'RGB': img = img.convert('RGB')
            if img.height > 800 or img.width > 800:
                img.thumbnail((800, 800))
            output = BytesIO()
            img.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = File(output, name=os.path.basename(self.image.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class TechnicalSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    key = models.CharField(max_length=100, verbose_name="ویژگی")
    value = models.CharField(max_length=255, verbose_name="مقدار")

# --- مدل جدید خدمات ---
class Service(models.Model):
    # لیست آیکون‌های پیشنهادی برای انتخاب راحت کاربر
    ICON_CHOICES = [
        ('fas fa-tools', 'آچار و ابزار (تعمیرات)'),
        ('fas fa-cogs', 'چرخ‌دنده (اورهال)'),
        ('fas fa-project-diagram', 'دیاگرام (پایپینگ)'),
        ('fas fa-headset', 'هدفون (پشتیبانی)'),
        ('fas fa-gas-pump', 'پمپ (جایگاه CNG)'),
        ('fas fa-check-shield', 'سپر (ایمنی و بازرسی)'),
        ('fas fa-truck', 'کامیون (حمل و نقل)'),
        ('fas fa-industry', 'کارخانه (نصب و راه‌اندازی)'),
        ('fas fa-oil-can', 'روغن‌دان (سرویس دوره‌ای)'),
    ]

    title = models.CharField(max_length=200, verbose_name="عنوان خدمت")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="آدرس سئو")
    
    # تغییر این فیلد به انتخاب‌گر (Choices)
    icon_class = models.CharField(
        max_length=50, 
        choices=ICON_CHOICES, 
        default='fas fa-tools', 
        verbose_name="انتخاب آیکون"
    )
    
    short_description = models.TextField(verbose_name="توضیح کوتاه صفحه اصلی")
    full_description = models.TextField(verbose_name="توضیح کامل صفحه اختصاصی")
    
    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title


class ServiceRequest(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    company_name = models.CharField(max_length=150, blank=True, verbose_name="نام شرکت")
    service_type = models.CharField(max_length=150, verbose_name="نوع خدمت")
    message = models.TextField(blank=True, verbose_name="توضیحات تکمیلی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "درخواست خدمت"
        verbose_name_plural = "درخواست‌های خدمت"

    def __str__(self):
        return f"{self.full_name} - {self.service_type}"
