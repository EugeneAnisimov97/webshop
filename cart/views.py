from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from tovars.models import Tovars
from django.contrib.auth.decorators import login_required


def get_cart(request):
    return request.session.get('cart', {})

def add_to_cart(request, tovar_id):
    cart = get_cart(request)
    if tovar_id in cart:
        cart[tovar_id] += 1
    else:
        cart[tovar_id] = 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_cart(request)
    cart_items = []
    
    tovar_ids = list(cart.keys())
    tovars = Tovars.objects.filter(id__in=tovar_ids)

    tovar_dict = {tovar.id: tovar for tovar in tovars}
    total_sum = 0 
    
    for tovar_id, quantity in cart.items():
        tovar = tovar_dict.get(int(tovar_id))
        if tovar:  # Проверка на случай, если товар не найден
            cart_items.append({'tovar': tovar, 'quantity': quantity})
            total_sum += tovar.price * quantity
    context = {
        'cart_items': cart_items,
        'total_cart_sum': total_sum,
    }
    return render(request, 'cart/cart_detail.html', context)

def cart_add_quantity(request, tovar_id):
    cart = get_cart(request)
    cart[str(tovar_id)] += 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_reduce_quantity(request, tovar_id):
    cart = get_cart(request)
    if cart[str(tovar_id)] > 1:
        cart[str(tovar_id)] -= 1
    else:
        del cart[str(tovar_id)]  # Удаляем товар, если количество 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_remove(request, tovar_id):
    cart = get_cart(request)
    if str(tovar_id) in cart:
        del cart[str(tovar_id)]  # Удаление товара из корзины
    request.session['cart'] = cart
    return redirect('cart_detail')