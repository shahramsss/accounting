from django import forms


class UserLoginForm(forms.Form):
    user_name = forms.CharField(label='نام کاربری' ,widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
