from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:val>', views.CategoryView, name="category"),
    path('product-detail/<int:pk>', views.ProductDetail, name="product-detail"),
    path('addtocart/', views.add_to_cart, name="addtocart"),
    path('cart/', views.show_cart, name="showcart"),
    path('checkout/', views.show_cart, name="checkout"),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
]