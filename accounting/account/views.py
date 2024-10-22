from django.shortcuts import render , redirect
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class LoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["user_name"], password=cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "شما با موفقیت وارد شدید.", "success")
                return redirect("home:home")
            else:
                messages.warning(request, "نام کاربری یا رمز عبور نادرست است!", "warning")
                return redirect("account:login")

    def get(self, request):
        form = UserLoginForm()
        return render(request, "account/login.html", {"form": form})


class LogoutView(View):
    def get(self , request):
        logout(request)
        messages.success(request, "شما خارج شدید.", "primary")
        return redirect("account:login")
        
        
        