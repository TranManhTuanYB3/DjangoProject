from django.contrib import admin
from .models import Product, MilkProduct, Cart, OrderPlaced, Wishlist

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'images')

@admin.register(MilkProduct)
class MilkProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category','images')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'mproduct', 'quantity')

@admin.register(OrderPlaced)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'product', 'mproduct', 'quantity','ordered_date', 'status')

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'mproduct')