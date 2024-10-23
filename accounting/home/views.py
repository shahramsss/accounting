from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product
from .forms import *
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html")


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "home/products.html", {"products": products})


class ProductRegisterView(View):
    form_class = ProductRegisterForm

    def get(self, request):
        return render(request, "home/product_register.html", {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " محصول با موفقیت ثبت شد.", "success")
            return redirect("home:products")
        else:
            messages.warning(request, " محصول با موفقیت ثبت شد.", "warning")
            return redirect("home:product_register")


class ProductDeleteView(View):
    pass


class ProductUpdateView(View):
    form_class = ProductRegisterForm

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = self.form_class(request.POST, instance=product)
        return render(request , '' , {'form':form})
