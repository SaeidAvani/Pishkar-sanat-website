from django.db import models

# ۱. دسته‌بندی محصولات (مثل: کمپرسور، قطعات یدکی)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="آدرس سئو (Slug)")
    
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


# ۲. محصولات (تجهیزات فیزیکی برای فروش)
class Product(models.Model):
    TYPE_CHOICES = (
        ('screw', 'اسکرو (Screw)'),
        ('piston', 'پیستونی (Piston)'),
        ('portable', 'معدنی/پرتابل'),
        ('dryer', 'درایر/خشک‌کن'),
        ('filter', 'فیلتر و قطعات مصرفی'),
        ('generator', 'ژنراتور اکسیژن/نیتروژن'),
        ('other', 'سایر تجهیزات'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="دسته‌بندی")
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    model_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='other', verbose_name="نوع دستگاه")
    description = models.TextField(verbose_name="توضیحات فنی")
    capacity = models.CharField(max_length=100, blank=True, null=True, verbose_name="ظرفیت/توان (اختیاری)")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر محصول")
    is_active = models.BooleanField(default=True, verbose_name="موجود/نمایش داده شود")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name


# ۳. خدمات (جدید: شامل پشتیبانی تلفنی، اورهال، لوله‌کشی)
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان خدمت")
    # مثلا: پشتیبانی فنی تلفنی (CNG)
    description = models.TextField(verbose_name="توضیحات کامل خدمت")
    image = models.ImageField(upload_to='services/', verbose_name="تصویر مرتبط", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="نمایش در سایت")

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات ما"

    def __str__(self):
        return self.title


# ۴. مشتریان و پروژه‌ها
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شرکت/بیمارستان")
    logo = models.ImageField(upload_to='clients/', verbose_name="لوگو")
    show_on_home = models.BooleanField(default=True, verbose_name="نمایش در صفحه اصلی")

    class Meta:
        verbose_name = "مشتری/پروژه"
        verbose_name_plural = "مشتریان"

    def __str__(self):
        return self.name


# ۵. فرم درخواست (اصلاح شده برای شامل شدن درخواست پشتیبانی)
class ServiceRequest(models.Model):
    REQUEST_TYPES = (
        ('repair', 'درخواست تعمیرکار (حضوری)'),
        ('support_call', 'پشتیبانی و مشاوره تلفنی'),
        ('purchase', 'مشاوره خرید'),
        ('installation', 'نصب و راه‌اندازی'),
    )
    
    STATUS_CHOICES = (
        ('new', 'جدید - بررسی نشده'),
        ('pending', 'در حال هماهنگی'),
        ('done', 'انجام شد'),
    )

    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES, default='repair', verbose_name="نوع درخواست")
    machine_model = models.CharField(max_length=100, verbose_name="مدل دستگاه (اختیاری)", blank=True)
    description = models.TextField(verbose_name="شرح مشکل یا درخواست")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="وضعیت")

    class Meta:
        verbose_name = "درخواست مشتری"
        verbose_name_plural = "درخواست‌های مشتریان"

    def __str__(self):
        return f"{self.full_name} ({self.get_request_type_display()})"