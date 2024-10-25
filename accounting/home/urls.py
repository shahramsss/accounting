"""
URL configuration for accounting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path 
from . import views


app_name = 'home'
urlpatterns = [
    path("home/" , views.HomeView.as_view() , name='home'),
    path("products/" , views.ProductsView.as_view() , name='products'),
    path("productregister/" , views.ProductRegisterView.as_view() , name='product_register'),
    path("productupdate/<int:pk>/" , views.ProductUpdateView.as_view() , name='product_update'),
    path("productdelete/<int:pk>/" , views.ProductDeleteView.as_view() , name='product_delete'),
    path("productdeleteconfirm/<int:pk>/" , views.ProductDeleteView.as_view() , name='product_delete_confirm'),
    #  warehouses urls
    path("warehouses/" , views.WarehousesView.as_view() , name='warehouses'),
    path("warehouseregister/" , views.WarehouseRegisterView.as_view() , name='warehouse_register'),
    path("warehouseupdate/<int:pk>/" , views.WarehouseUpdateView.as_view() , name='warehouse_update'),
    path("warehousedelete/<int:pk>/" , views.WarehouseDeleteView.as_view() , name='warehouse_delete'),
    path("warehousedeleteconfirm/<int:pk>/" , views.WarehouseDeleteView.as_view() , name='warehouse_delete_confirm'),
    # stocks urls
    path("stocks/" , views.StoksView.as_view() , name='stocks'),
    path("stockregister/" , views.StockRegisterView.as_view() , name='stock_register'),
    path("stockupdate/<int:pk>/" , views.StockUpdateView.as_view() , name='stock_update'),
    path("stockdelete/<int:pk>/" , views.StocksDeleteView.as_view() , name='stock_delete'),
    path("stockdeleteconfirm/<int:pk>/" , views.StocksDeleteView.as_view() , name='stock_delete_confirm'),
    # Invoice urls
    path("invoices/" , views.InvoicesView.as_view() , name='invoices'),
    path("invoiceregister/" , views.InvoiceRegisterView.as_view() , name='invoice_register'),
    path("invoiceupdate/<int:pk>/" , views.InvoiceUpdateView.as_view() , name='invoice_update'),
    path("invoicedelete/<int:pk>/" , views.InvoiceDeleteView.as_view() , name='invoice_delete'),
    path("invoicedeleteconfirm/<int:pk>/" , views.InvoiceDeleteView.as_view() , name='invoice_delete_confirm'),
    # invoice_item urls
    path("invoiceitems/" , views.InvoiceItemsView.as_view() , name='invoice_items'),
    path("invoicitemeregister/" , views.InvoiceItemRegisterView.as_view() , name='invoice_item_register'),

]
