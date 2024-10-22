from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PersonRegisterForm
from .models import Person


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
                messages.warning(
                    request, "نام کاربری یا رمز عبور نادرست است!", "warning"
                )
                return redirect("account:login")

    def get(self, request):
        form = UserLoginForm()
        return render(request, "account/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "شما خارج شدید.", "primary")
        return redirect("account:login")


class PersonRegisterView(View):
    form_class = PersonRegisterForm

    def get(self, request):
        return render(
            request, "account/pesron_register.html", {"form": self.form_class}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ثبت شخص با موفقت انجام شد.", "success")
            return redirect("account:persons")
        else:
            messages.warning(request, "ثبت نام انجام نشد دوباره تلاش کنید!", "warning")
            return redirect("account:person_register")


class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(
            request,'account/pesrons.html' ,{'persons':persons}
        )


class PersonUpdateView(View):
    form_class = PersonRegisterForm

    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = self.form_class(instance=person)
        return render(request, "account/pesron_update.html", {"form": form})

    def post(self , request , pk):
        person = get_object_or_404(Person, pk=pk)
        form = self.form_class(request.POST , instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, "ویرایش با موفقت انجام شد.", "success")
            return redirect("account:persons")
        else:
            messages.warning(request, "ویرایش انجام نشد دوباره تلاش کنید!", "warning")
            return redirect("account:person_update" ,pk = person.id)


