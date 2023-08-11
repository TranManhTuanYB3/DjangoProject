from django.contrib import admin
from .models import Product, MilkProduct, Cart

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'images')

@admin.register(MilkProduct)
class MilkProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category','images')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
