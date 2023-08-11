from django.shortcuts import render, redirect
from .models import Product, MilkProduct, Cart
from django.http import JsonResponse, HttpResponseBadRequest
from django.db.models import Q

def home(request):
    return render(request, 'main/home.html')

def CategoryView(request, val):
    products = Product.objects.filter(category=val)
    title = products.values('title')
    context = {
        'val': val,
        'products': products,
        'title': title,
    }
    return render(request, 'main/category.html', context)

def ProductDetail(request, pk):
    products = Product.objects.get(pk=pk)
    mproducts = MilkProduct.objects.filter(category=products)
    context = {
        'products': products,
        'mproducts': mproducts,
    }
    return render(request, 'main/productdetail.html', context)

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    if product.price is None:
        product = MilkProduct.objects.get(id=product_id)
    Cart.objects.create(user=user, product=product)
    return redirect('/cart')

def show_cart(request):
    product_id = request.GET.get('prod_id')
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    amount = 0
    for p in cart_items:
        if p.product.price is not None:
            value = p.quantity * p.product.price
        else:
            value = p.quantity * 7000
        amount += value
    totalamount = amount + 23000

    return render(request, 'main/addtocart.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user

        # Sử dụng filter() để lấy danh sách các sản phẩm trong giỏ hàng
        cart_items = Cart.objects.filter(product=prod_id, user=user)

        if cart_items.exists():
            cart_item = cart_items.first()  # Lấy đối tượng đầu tiên trong danh sách

            cart_item.quantity += 1
            cart_item.save()

            # Tính lại thông tin giỏ hàng
            amount = 0
            for p in cart_items:
                if p.product.price is not None:
                    value = p.quantity * p.product.price
                else:
                    value = p.quantity * 7000
                amount += value
            totalamount = amount + 23000

            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user

        # Sử dụng filter() để lấy danh sách các sản phẩm trong giỏ hàng
        cart_items = Cart.objects.filter(product=prod_id, user=user)

        if cart_items.exists():
            cart_item = cart_items.first()  # Lấy đối tượng đầu tiên trong danh sách

            cart_item.quantity -= 1
            cart_item.save()

            # Tính lại thông tin giỏ hàng
            amount = 0
            for p in cart_items:
                if p.product.price is not None:
                    value = p.quantity * p.product.price
                else:
                    value = p.quantity * 7000
                amount += value
            totalamount = amount + 23000

            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user

        # Sử dụng filter() để lấy danh sách các sản phẩm trong giỏ hàng
        cart_items = Cart.objects.filter(product=prod_id, user=user)

        if cart_items.exists():
            cart_item = cart_items.first()  # Lấy đối tượng đầu tiên trong danh sách

            
            cart_item.delete()

            # Tính lại thông tin giỏ hàng
            amount = 0
            for p in cart_items:
                if p.product.price is not None:
                    value = p.quantity * p.product.price
                else:
                    value = p.quantity * 7000
                amount += value
            totalamount = amount + 23000

            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)