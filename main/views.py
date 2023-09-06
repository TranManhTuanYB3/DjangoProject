from django.shortcuts import render, redirect
from .models import Product, MilkProduct, Cart, OrderPlaced, Wishlist
from account.models import Customer
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q


def home(request):
    user=request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))
    return render(request, 'main/home.html', locals())

def CategoryView(request, val):
    user=request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    products = Product.objects.filter(category=val)
    title = products.values('title')
    return render(request, 'main/category.html', locals())

def ProductDetail(request, pk):
    user=request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    products = Product.objects.get(pk=pk)
    mproducts = MilkProduct.objects.filter(category=products)
    wishlist = Wishlist.objects.filter(user=user, product=products)
    
    return render(request, 'main/productdetail.html', locals())

def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect("/must_authenticate")
    
    user = request.user
    product_id = request.GET.get('prod_id')
    mproduct_id = request.GET.get('mprod_id')
    product = Product.objects.get(id=product_id)
    if product.id >10:
        if Cart.objects.filter(user=user, product_id=product_id).exists():
            cart_item = Cart.objects.get(user=user, product_id=product_id)
            cart_item.quantity += 1
            cart_item.save()
        else:
            Cart.objects.create(user=user, product=product)
    else:
        if Cart.objects.filter(user=user, mproduct_id=mproduct_id).exists():
            cart_item = Cart.objects.get(user=user, mproduct_id=mproduct_id)
            cart_item.quantity += 1
            cart_item.save()
        else:
            mproduct = MilkProduct.objects.get(id=mproduct_id)
            Cart.objects.create(user=user, product=mproduct.category, mproduct=mproduct)
    return redirect('/cart')

def show_cart(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    if not request.user.is_authenticated:
        return redirect("/must_authenticate")
    
    
    cart_items = Cart.objects.filter(user=user)
    amount = 0
    for p in cart_items:
        if p.product.id > 10:
            value = p.quantity * p.product.price
        else:
            value = p.quantity * p.mproduct.price
        amount += value
    totalamount = amount + 23000

    return render(request, 'main/addtocart.html', locals())

def check_out(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    if not request.user.is_authenticated:
        return redirect("/must_authenticate")
    
    
    add = Customer.objects.filter(user=user)

    if not add.exists():
        messages.error(request, 'Lỗi: Chưa có địa chỉ nhận hàng.')
        return render(request, 'account/checkaddress.html')

    cart_items = Cart.objects.filter(user=user)
    famount = 0
    for p in cart_items:
        if p.product.id > 10:
            value = p.quantity * p.product.price
        else:
            value = p.quantity * p.mproduct.price
        famount += value
    totalamount = famount + 23000

    return render(request, 'main/checkout.html', locals())

def create_orders(request):
    if not request.user.is_authenticated:
        return redirect("/must_authenticate")

    user = request.user
    customer_id = request.POST.get('cust_id')
    customer = Customer.objects.get(id=customer_id)
    cart_items = Cart.objects.filter(user=user)
    
    for c in cart_items:        
        OrderPlaced.objects.create(
            user=user,
            customer=customer,
            product=c.product,
            mproduct=c.mproduct,
            quantity=c.quantity,
            status='Pending',
        )
        c.delete()
    return redirect('/orders')

def orders(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))

    if not request.user.is_authenticated:
        return redirect("/must_authenticate") 

    order_placed = OrderPlaced.objects.filter(user=user)
    return render(request, 'main/orders.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        user = request.user
        product_id = request.GET.get('prod_id')
        mproduct_id = request.GET.get('mprod_id')
        product = Product.objects.get(id=product_id)
        
        cart_item = Cart.objects.get(user=user, product_id=product_id)
        cart_item.quantity += 1
        cart_item.save()     

        cart_items = Cart.objects.filter(user=user)
        amount = 0
        for p in cart_items:
            if p.product.id > 10:
                value = p.quantity * p.product.price
            else:
                value = p.quantity * p.mproduct.price
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
        product_id = request.GET.get('prod_id')
        user = request.user
        
        cart_item = Cart.objects.get(product_id=product_id, user=user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

            cart_items = Cart.objects.filter(user=user)
            amount = 0
            for p in cart_items:
                if p.product.id > 10:
                    value = p.quantity * p.product.price
                else:
                    value = p.quantity * p.mproduct.price
                amount += value
            totalamount = amount + 23000

            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)

def wish_list(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))
    
    if not request.user.is_authenticated:
        return redirect("/must_authenticate") 
    
    wishlist = Wishlist.objects.filter(user=user)
    return render(request, 'main/wishlist.html', locals())
    
def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET.get('prod_id')
        user = request.user
        
        cart_item = Cart.objects.get(product_id=product_id, user=user)
        cart_item.delete()

        cart_items = Cart.objects.filter(user=user)
        amount = 0
        for p in cart_items:
            if p.product.id > 10:
                value = p.quantity * p.product.price
            else:
                value = p.quantity * p.mproduct.price
            amount += value
        totalamount = amount + 23000

        data = {
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)
    
def plus_wishlist(request):
    if request.method == 'GET':
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Wishlist.objects.create(user=user, product=product)
       
        data = {
            'message':'Wishlist Added Successfully',
        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == 'GET':
        user = request.user
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Wishlist.objects.filter(user=user, product=product).delete()
       
        data = {
            'message':'Wishlist Removed Successfully',
        }
        return JsonResponse(data)
    
def search(request):
    query = request.GET['search']
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=user))
        wishitem = len(Wishlist.objects.filter(user=user))
    
    product = Product.objects.filter(title__icontains=query)
    return render(request, 'main/search.html', locals())
