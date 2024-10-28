from django import forms
from .models import Product, Warehouse, Stock, Invoice, InvoiceItem
from django.core.exceptions import ValidationError


class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "نام محصول"}
            ),
            "price": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "قیمت فروش"}
            ),
            "cost_price": forms.TextInput(
                attrs={"class": "form-control", "rows": 3, "placeholder": "قیمت خرید"}
            ),
        }

        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "name": "نام محصول",
            "price": "قیمت فروش",
            "cost_price": "قیمت خرید ",
        }


class WarehouseRegisterForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "نام انبار"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "آدرس انبار"}
            ),
        }

        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "name": "نام انبار",
            "location": "آدرس انبار",
        }


class StockeRegisterForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

        widgets = {
            "product": forms.Select(
                attrs={"class": "form-control"}
            ),  # ویجت انتخاب برای محصول
            "warehouse": forms.Select(
                attrs={"class": "form-control"}
            ),  # ویجت انتخاب برای انبار
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),  # ورودی عددی برای مقدار موجودی
        }
        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "product": "نام محصول",
            "warehouse": "نام انبار",
            "quantity": "تعداد",
        }


class StockeUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

        widgets = {
            "product": forms.Select(
                attrs={"class": "form-control"}
            ),  # ویجت انتخاب برای محصول
            "warehouse": forms.Select(
                attrs={"class": "form-control"}
            ),  # ویجت انتخاب برای انبار
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),  # ورودی عددی برای مقدار موجودی
        }
        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "product": "نام محصول",
            "warehouse": "نام انبار",
            "quantity": "تعداد",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # غیر قابل تغییر کردن فیلدها
        self.fields["product"].disabled = True
        self.fields["warehouse"].disabled = True


class InvoiceRegisterForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"

        widgets = {
            "invoice_type": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "person": forms.Select(attrs={"class": "form-control", "min": 0}),
        }
        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "invoice_type": "نوع فاکتور",
            "date": "تاریخ",
            "person": "شخص",
        }


class InvoiceItemRegisterForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = "__all__"

        widgets = {
            "invoice": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "warehouse": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "تعداد"}
            ),
            "unit_price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "قیمت واحد"}
            ),
        }

        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            "invoice": "فاکتور",
            "product": "محصول",
            "warehouse": "انبار",
            "quantity": "تعداد",
            "unit_price": "قیمت واحد",
        }

      