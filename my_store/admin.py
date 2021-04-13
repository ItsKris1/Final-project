from django.contrib import admin
from .models import Product, Category, Profile, OrderItem, Order, Address

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)

admin.site.register(OrderItem)
admin.site.register(Order)

admin.site.register(Address)


