from django.contrib import admin
from .models import Offers, Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
# Register your models here.

admin.site.register(Product,ProductAdmin)
admin.site.register(Offers)