from django import forms
from .models import Person


class UserLoginForm(forms.Form):
    user_name = forms.CharField(
        label="نام کاربری", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="رمز عبور", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class PersonRegisterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "phone", "address",]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "نام و نام خانوادگی"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "موبایل"}
            ),
            "address": forms.Textarea(
                attrs={"class": "form-control", "rows": 3, "placeholder": "آدرس"}
            ),
        }

        labels = {  # برچسب‌های سفارشی برای فیلدهای موجود در مدل
            'name': 'نام',
            'phone': 'تلفن همراه',
            'address': 'آدرس',
        }
