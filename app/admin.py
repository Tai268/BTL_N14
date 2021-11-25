from django.contrib import admin

# Register your models here.
from .models import Category, Sub_Category, Product, Contact_us, Order

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_us)
admin.site.register(Order)

