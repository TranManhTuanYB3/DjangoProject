from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:val>', views.CategoryView, name="category"),
    path('product-detail/<int:pk>', views.ProductDetail, name="product-detail"),
    path('addtocart/', views.add_to_cart, name="addtocart"),
    path('cart/', views.show_cart, name="showcart"),
    path('checkout/', views.check_out, name="checkout"),
    path('create_orders/', views.create_orders, name="create_orders"),
    path('orders/', views.orders, name="orders"),
    path('wishlist/', views.wish_list, name="wishlist"),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('pluswishlist/', views.plus_wishlist, name="pluswishlist"),
    path('minuswishlist/', views.minus_wishlist, name="minuswishlist"),

    path('search/', views.search, name="search"),
]