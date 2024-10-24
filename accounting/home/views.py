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
            messages.warning(request, " محصول ثبت نشد دوباره تلاش کنید!", "warning")
            return redirect("home:product_register")


class ProductUpdateView(View):
    form_class = ProductRegisterForm

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = self.form_class(instance=product)
        return render(request, "home/product_update.html", {"form": form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = self.form_class(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, " محصول با موفقیت ویرایش شد.", "success")
            return redirect("home:products")
        else:
            messages.warning(request, " محصول ویرایش نشد دوباره تلاش کنید!", "warning")
            return redirect("home:product_update", pk=product.id)


class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, "home/product_delete.html", {"product": product})

    def post(self , request , pk):
        product = get_object_or_404(Product, pk=pk)
        if 'confirm_delete'  in request.POST:
            product.delete()
            messages.success(request , 'محصول با موفقیت حذف شد.','success')
            return redirect("home:products")
        else:
            messages.warning(request , 'محصول  حذف نشد!.','warning')
            return redirect("home:products")

