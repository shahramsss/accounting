from django import forms
from .models import Product, Warehouse , Stock , Invoice


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
            'product': forms.Select(attrs={'class': 'form-control'}),  # ویجت انتخاب برای محصول
            'warehouse': forms.Select(attrs={'class': 'form-control'}),  # ویجت انتخاب برای انبار
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),  # ورودی عددی برای مقدار موجودی
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
            'product': forms.Select(attrs={'class': 'form-control'}),  # ویجت انتخاب برای محصول
            'warehouse': forms.Select(attrs={'class': 'form-control'}),  # ویجت انتخاب برای انبار
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),  # ورودی عددی برای مقدار موجودی
        }
        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
                    "product": "نام محصول",
                    "warehouse": "نام انبار",
                    "quantity": "تعداد",
                }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # غیر قابل تغییر کردن فیلدها
        self.fields['product'].disabled = True
        self.fields['warehouse'].disabled = True
        
class InvoiceRegisterForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"