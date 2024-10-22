from django.contrib import admin
from .models import Invoice , InvoiceItem , Product , Stock , Warehouse


admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Warehouse)
