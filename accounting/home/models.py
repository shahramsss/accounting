from django.db import models
from account.models import Person
from django.utils import timezone
from khayyam import JalaliDate
from django.db import models

# مدل محصول
class Product(models.Model):
    name = models.CharField(max_length=200)  # نام محصول
    price = models.DecimalField(max_digits=10, decimal_places=0)  # قیمت محصول (برای فروش)
    cost_price = models.DecimalField(max_digits=10, decimal_places=0)  # قیمت خرید محصول

    def __str__(self):
        return self.name

# مدل انبار
class Warehouse(models.Model):
    name = models.CharField(max_length=100)  # نام انبار
    location = models.CharField(max_length=200, blank=True, null=True)  # موقعیت انبار (اختیاری)

    def __str__(self):
        return self.name

# مدل موجودی (برای مدیریت موجودی هر محصول در هر انبار)
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)  # محصول مربوطه
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)  # انبار مربوطه
    quantity = models.PositiveIntegerField(default=0)  # مقدار موجودی

    class Meta:
        unique_together = ('product', 'warehouse')  # هر محصول در هر انبار تنها یک بار ظاهر می‌شود

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name}: {self.quantity}"


# مدل فاکتور (هم خرید و هم فروش)
class Invoice(models.Model):
    INVOICE_TYPE_CHOICES = [
        ('purchase', 'خرید'),  # فاکتور خرید
        ('sale', 'فروش')  # فاکتور فروش
    ]

    invoice_type = models.CharField(max_length=10, choices=INVOICE_TYPE_CHOICES)  # نوع فاکتور
    date = models.DateField(default=timezone.now)  # تاریخ فاکتور
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='invoices')  # شخص (فروشنده یا خریدار)

    def __str__(self):
        return f"#{self.id} - {self.person.name} -{self.invoice_type} - ({JalaliDate(self.date).strftime("%D %B %Y")}) "
    # محاسبه کل مبلغ فاکتور
    @property
    def total_amount(self):
        total = sum(item.total_price for item in self.items.all())
        return total

# مدل آیتم‌های فاکتور (برای خرید و فروش)
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='items')  # ارتباط با فاکتور
    product = models.ForeignKey(Product, on_delete=models.PROTECT)  # ارتباط با محصول
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT   )  # انبار مربوطه
    quantity = models.PositiveIntegerField()  # تعداد محصول
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)  # قیمت هر واحد (می‌تواند قیمت خرید یا قیمت فروش باشد)

    # محاسبه قیمت کل برای هر آیتم در فاکتور
    @property
    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Invoice #{self.invoice.id})"

    # # کاهش یا افزایش موجودی انبار بر اساس خرید یا فروش
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # ذخیره آیتم فاکتور

    #     # به‌روزرسانی موجودی انبار
    #     stock, created = Stock.objects.get_or_create(product=self.product, warehouse=self.warehouse)
        
    #     if self.invoice.invoice_type == 'sale':
    #         stock.quantity -= self.quantity  # کاهش موجودی در صورت فروش
    #     elif self.invoice.invoice_type == 'purchase':
    #         stock.quantity += self.quantity  # افزایش موجودی در صورت خرید

    #     stock.save()  # ذخیره به‌روزرسانی موجودی


