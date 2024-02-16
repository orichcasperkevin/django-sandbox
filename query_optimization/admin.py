from django.contrib import admin

from .models import Attribute,Product,ProductAtrribute,Customer,Order
# Register your models here.
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAtrribute)
admin.site.register(Customer)
admin.site.register(Order)