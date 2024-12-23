from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Warehouse, Stock, Invoice, InvoiceItem
from .forms import *
from django.contrib import messages
from django.db.models import ProtectedError
from django.db import transaction
from django.core.paginator import Paginator

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
            try:
                product.delete()
                messages.success(request, "محصول با موفقیت حذف شد.", "success")
                return redirect("home:products")
            except ProtectedError as e:
                messages.error(
                    request,
                    "این محصول دارای موجودی می باشد و قابل حذف نیست!",
                    "warning",
                )
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
            messages.warning(
                request,
                "موجودی ثبت نشد! این محصول در این انبار قبلا ثبت شده است!",
                "warning",
            )
            return redirect("home:stock_register")


class StockUpdateView(View):
    form_class = StockeUpdateForm

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


class StocksDeleteView(View):
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, "home/stock_delete.html", {"stock": stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        if "stock_confirm_delete" in request.POST:
            stock.delete()
            messages.success(request, "انبار با موفقیت حذف شد.", "success")
            return redirect("home:stocks")
        else:
            messages.warning(request, "انبار حذف نشد!.", "warning")
            return redirect("home:stocks")


# Invoice View
class InvoicesView(View):
    def get(self, request):
        invoices = Invoice.objects.all().order_by("-date")
        return render(request, "home/invoices.html", {"invoices": invoices})


class InvoiceRegisterView(View):
    form_class = InvoiceRegisterForm

    def get(self, request):
        return render(request, "home/invoice_register.html", {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "فاکتور با موفقیت ثبت شد.", "success")
            return redirect("home:invoices")
        else:
            messages.warning(
                request,
                "فاکتور ثبت نشد!",
                "warning",
            )
            return redirect("home:invoice_register")


class InvoiceUpdateView(View):
    form_class = InvoiceRegisterForm

    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        form = self.form_class(instance=invoice)
        return render(request, "home/invoice_update.html", {"form": form})

    def post(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        form = self.form_class(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            messages.success(request, "فاکتور با موفقیت ویرایش شد.", "success")
            return redirect("home:invoices")
        else:
            messages.success(request, "فاکتور ویرایش نشد!.", "warning")
            return redirect("home:invoice_register")


class InvoiceDeleteView(View):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        return render(request, "home/invoice_delete.html", {"invoice": invoice})

    def post(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        if "invoice_confirm_delete" in request.POST:
            invoice.delete()
            messages.success(request, "فاکتور با موفقیت حذف شد.", "success")
            return redirect("home:invoices")
        else:
            messages.warning(request, "افاکتور حذف نشد!.", "warning")
            return redirect("home:invoices")


# InvoiceItem View
class InvoiceItemsView(View):
    def get(self, request):
        invoice_items_all = InvoiceItem.objects.all()
        paginator = Paginator(invoice_items_all, 20)  
        page_number = request.GET.get('page')
        invoice_items = paginator.get_page(page_number)
        return render(
            request, "home/invoice_items.html", {"invoice_items": invoice_items}
        )


class InvoiceItemRegisterView(View):
    form_class = InvoiceItemRegisterForm

    def get(self, request):
        return render(
            request, "home/invoice_item_register.html", {"form": self.form_class}
        )

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # دریافت داده‌های تمیز شده از فرم
            warehouse = form.cleaned_data["warehouse"]
            product = form.cleaned_data["product"]
            quantity = form.cleaned_data["quantity"]
            incoive = form.cleaned_data["invoice"]
            try:
                # بررسی موجودی انبار
                stock = Stock.objects.get(warehouse=warehouse, product=product)
                if incoive.invoice_type == "sale" and quantity > stock.quantity:
                    messages.warning(
                        request,
                        f"موجودی کافی برای {product.name} در انبار {warehouse.name} وجود ندارد. "
                        f"موجودی فعلی: {stock.quantity}",
                        "warning",
                    )
                    return render(
                        request, "home/invoice_item_register.html", {"form": form}
                    )

            except Stock.DoesNotExist:
                messages.warning(
                    request,
                    f"محصول {product.name} در انبار {warehouse.name} موجود نیست.",
                    "warning",
                )
                return render(
                    request, "home/invoice_item_register.html", {"form": form}
                )

            # ذخیره آیتم و به‌روزرسانی موجودی انبار
            if incoive.invoice_type == "sale":
                stock.quantity -= quantity
            else:
                stock.quantity += quantity
            stock.save()
            form.save()
            messages.success(request, "مورد با موفقیت ثبت شد.", "success")
            return redirect("home:invoice_items")

        # در صورت نامعتبر بودن فرم
        messages.warning(request, "موردی ثبت نشد!", "warning")
        return render(request, "home/invoice_item_register.html", {"form": form})


class InvoicItemeUpdateView(View):
    form_class = InvoiceItemRegisterForm

    def get(self, request, pk):
        invoice_item = get_object_or_404(InvoiceItem, pk=pk)
        form = self.form_class(instance=invoice_item)
        return render(request, "home/invoice_item_update.html", {"form": form})

    def post(self, request, pk):
        invoice_item = get_object_or_404(InvoiceItem, pk=pk)
        stock = Stock.objects.get(
            product=invoice_item.product, warehouse=invoice_item.warehouse
        )
        stock_quantity = stock.quantity
        form = self.form_class(request.POST, instance=invoice_item)
        previous_quantity = invoice_item.quantity

        if form.is_valid():
            new_quantity = form.cleaned_data["quantity"]
            dif_quantity = previous_quantity - new_quantity

            if dif_quantity == 0:
                messages.success(request, "تغییری ایجاد نشد!", "success")
                return redirect("home:invoice_items")

            # تنظیم موجودی انبار بر اساس نوع فاکتور
            if invoice_item.invoice.invoice_type == "purchase":
                stock.quantity -= dif_quantity  # کاهش موجودی در خرید
            else:
                stock.quantity += dif_quantity  # افزایش موجودی در فروش

            # بررسی وضعیت موجودی بعد از تنظیم
            if stock.quantity < 0:
                messages.warning(
                    request,
                    f"موجودی کافی برای {invoice_item.product.name} در انبار {invoice_item.warehouse.name} وجود ندارد. "
                    f"موجودی فعلی: {stock_quantity}.",
                    "warning",
                )
                return redirect("home:invoice_item_update", invoice_item.id)

            # ذخیره تغییرات و نمایش پیام موفقیت
            stock.save()
            form.save()
            messages.success(request, "مورد با موفقیت ویرایش شد.", "success")
            return redirect("home:invoice_items")

        # در صورت نامعتبر بودن فرم
        messages.error(request, "خطایی در فرم رخ داده است.", "danger")
        return redirect("home:invoice_items")


class InvoiceItemDeleteView(View):
    def get(self, request, pk):
        invoice_item = get_object_or_404(InvoiceItem, pk=pk)
        return render(
            request, "home/invoice_item_delete.html", {"invoice_item": invoice_item}
        )

    def post(self, request, pk):
        invoice_item = get_object_or_404(InvoiceItem, pk=pk)

        if "invoice_item_confirm_delete" not in request.POST:
            messages.warning(request, "مورد فاکتور حذف نشد!", "warning")
            return redirect("home:invoice_items")

        # بازیابی موجودی مربوط به محصول و انبار
        stock = Stock.objects.get(
            product=invoice_item.product, warehouse=invoice_item.warehouse
        )

        # تنظیم موجودی بر اساس نوع فاکتور
        if invoice_item.invoice.invoice_type == "purchase":
            stock.quantity -= invoice_item.quantity  # کاهش موجودی برای خرید
        else:
            stock.quantity += invoice_item.quantity  # افزایش موجودی برای فروش

        # بررسی اینکه موجودی منفی نشود
        if stock.quantity < 0:
            messages.warning(
                request,
                f"موجودی کافی برای حذف {invoice_item.product.name} در انبار {invoice_item.warehouse.name} وجود ندارد. "
                f"موجودی فعلی: {stock.quantity + invoice_item.quantity}.",
                "warning",
            )
            return redirect("home:invoice_items")

        # ذخیره تغییرات و حذف آیتم
        stock.save()
        invoice_item.delete()
        messages.success(request, "مورد فاکتور با موفقیت حذف شد.", "success")
        return redirect("home:invoice_items")


class SearchView(View):
    def get(self, request):
        query = request.GET.get("query")
        invoices = (
            Invoice.objects.filter(person__name__icontains=query).order_by("-date") if query else []
        )
        return render(request, "home/search.html", {"invoices": invoices})


class InvoiceItemsPersonView(View):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        invoice_items = invoice.items.all()
        return render(
            request,
            "home/invoice_items_person.html",
            {"invoice_items": invoice_items, "invoice": invoice},
        )


class InvoiceItemInvoiceRegisterView(View):
    form_class = InvoiceItemRegisterForm

    def get(self, request, pk):
        query = request.GET.get('q')  # گرفتن مقدار جستجو از query string

        if query:
            # فیلتر کردن محصولات بر اساس بخشی از نام
            stocks = Stock.objects.filter(product__name__icontains=query)
        else:
            stocks = Stock.objects.all()
        invoice = get_object_or_404(Invoice, pk=pk)
        form = self.form_class(initial_invoice=invoice)
        return render(
            request, "home/invoice_item_invoice_register.html", {"form": form ,"stocks":stocks}
        )

    def post(self, request, pk):
        form = self.form_class(request.POST)
        invoice = get_object_or_404(Invoice, pk=pk)
        if form.is_valid():
            # دریافت داده‌های تمیز شده از فرم
            warehouse = form.cleaned_data["warehouse"]
            product = form.cleaned_data["product"]
            quantity = form.cleaned_data["quantity"]
            incoive = form.cleaned_data["invoice"]
            try:
                # بررسی موجودی انبار
                stock = Stock.objects.get(warehouse=warehouse, product=product)
                if incoive.invoice_type == "sale" and quantity > stock.quantity:
                    messages.warning(
                        request,
                        f"موجودی کافی برای {product.name} در انبار {warehouse.name} وجود ندارد. "
                        f"موجودی فعلی: {stock.quantity}",
                        "warning",
                    )
                    return render(
                        request, "home/invoice_item_register.html", {"form": form}
                    )

            except Stock.DoesNotExist:
                messages.warning(
                    request,
                    f"محصول {product.name} در انبار {warehouse.name} موجود نیست.",
                    "warning",
                )
                return render(
                    request, "home/invoice_item_register.html", {"form": form}
                )

            # ذخیره آیتم و به‌روزرسانی موجودی انبار
            if incoive.invoice_type == "sale":
                stock.quantity -= quantity
            else:
                stock.quantity += quantity
            stock.save()
            invoice_item = form.save(commit=False)
            invoice_item.unit_price = stock.product.price
            invoice_item.save()
            messages.success(request, "مورد با موفقیت ثبت شد.", "success")
            return redirect("home:invoice_items_pesron" , invoice.id)

        # در صورت نامعتبر بودن فرم
        messages.warning(request, "موردی ثبت نشد!", "warning")
        return render(request, "home/invoice_item_register.html", {"form": form})
