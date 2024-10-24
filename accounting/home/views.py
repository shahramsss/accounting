from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Warehouse, Stock
from .forms import *
from django.contrib import messages
from django.db.models import ProtectedError


# home viws
class HomeView(View):
    def get(self, request):
        return render(request, "home/home.html")


# product views
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

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if "confirm_delete" in request.POST:
            product.delete()
            messages.success(request, "محصول با موفقیت حذف شد.", "success")
            return redirect("home:products")
        else:
            messages.warning(request, "محصول حذف نشد!.", "warning")
            return redirect("home:products")


# Warehouses views
class WarehousesView(View):
    def get(self, request):
        warehouses = Warehouse.objects.all()
        return render(request, "home/warehouses.html", {"warehouses": warehouses})


class WarehouseRegisterView(View):
    form_class = WarehouseRegisterForm

    def get(self, request):
        return render(
            request, "home/warehouse_register.html", {"form": self.form_class}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "انبار با موفقیت ثبت شد.", "success")
            return redirect("home:warehouses")
        else:
            messages.success(request, "انبار ثبت نشد!", "warning")
            return redirect("home:warehouse_register")


class WarehouseUpdateView(View):
    form_class = WarehouseRegisterForm

    def get(self, request, pk):
        warehouse = get_object_or_404(Warehouse, pk=pk)
        form = self.form_class(instance=warehouse)
        return render(request, "home/warehouse_update.html", {"form": form})

    def post(self, request, pk):
        warehouse = get_object_or_404(Warehouse, pk=pk)
        form = self.form_class(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, "انبار با موفقیت ویرایش شد.", "success")
            return redirect("home:warehouses")
        else:
            messages.success(request, "انبار ویرایش نشد!.", "warning")
            return redirect("home:warehouseregister")


class WarehouseDeleteView(View):
    def get(self, request, pk):
        warehouse = get_object_or_404(Warehouse, pk=pk)
        return render(request, "home/warehouse_delete.html", {"warehouse": warehouse})

    def post(self, request, pk):
        warehouse = get_object_or_404(Warehouse, pk=pk)
        if "warehouse_confirm_delete" in request.POST:
            try:
                warehouse.delete()
                messages.success(request, "انبار با موفقیت حذف شد.", "success")
                return redirect("home:warehouses")
            except ProtectedError as e:
                # در صورتی که کلیدهای خارجی محافظت‌شده وجود داشته باشد
                messages.error(
                    request, "این انبار دارای محصول می باشد و قابل حذف نیست!", "warning"
                )
                return redirect("home:warehouses")
        else:
            messages.warning(request, "انبار حذف نشد!.", "warning")
            return redirect("home:warehouses")


# Stock View
class StoksView(View):
    def get(self, request):
        stocks = Stock.objects.all()
        return render(request, "home/stocks.html", {"stocks": stocks})


class StockRegisterView(View):
    form_class = StockeRegisterForm

    def get(self, request):
        return render(request, "home/stock_register.html", {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "موجودی با موفقیت ثبت شد.", "success")
            return redirect("home:stocks")
        else:
            messages.success(
                request,
                "موجودی ثبت نشد! این محصول در این انبار قبلا ثبت شده است!",
                "warning",
            )
            return redirect("home:stock_register")


class StockUpdateView(View):
    form_class = StockeRegisterForm

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        form = self.form_class(instance=stock)
        return render(request, "home/stock_update.html", {"form": form})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        form = self.form_class(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, "موجودی با ویرایش ثبت شد.", "success")
            return redirect("home:stocks")
        else:
            messages.success(
                request,
                "موجودی ویرایش نشد!",
                "warning",
            )
            return redirect("home:stock_update")
