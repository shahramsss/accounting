from django import forms
from .models import Product

class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

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
            'name': 'نام محصول',
            'price': 'قیمت فروش',
            'cost_price': 'قیمت خرید ',
        }