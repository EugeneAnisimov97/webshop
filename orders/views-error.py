from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Orders, OrderItem
from django.contrib import messages
from tovars.models import Tovars

def get_cart(request):
    return request.session.get('cart', {})

@login_required
def create_order(request):
    cart = get_cart(request)
    total_cart_sum = 0
    cart_items = []

    for tovar_id, quantity in cart.items():
        tovar = get_object_or_404(Tovars, id=tovar_id)
        total_cart_sum += tovar.price * quantity
        cart_items.append({'tovar': tovar, 'quantity': quantity})

    if request.method == 'POST':
        # Создаем заказ
        order = Orders.objects.create(user=request.user)

        for item in cart_items:
            tovar = item['tovar']
            if tovar.stock >= item['quantity']:
                tovar.stock -= item['quantity']
                tovar.save()
                # Создаем элемент заказа
                OrderItem.objects.create(order=order, tovar=tovar, quantity=item['quantity'])
            else:
                messages.error(request, f"Недостаточно товара: {tovar.name}. Доступно: {tovar.stock}, запрашиваемое: {item['quantity']}")
                return render(request, 'orders/create_order.html', {
                    'cart_items': cart_items,
                    'total_cart_sum': total_cart_sum,
                })

        # Очистка корзины после успешного создания заказа
        request.session['cart'] = {}
        return redirect('order_list')  # Перенаправление на страницу успешного заказа

    return render(request, 'orders/create_order.html', {
        'cart_items': cart_items,
        'total_cart_sum': total_cart_sum,
    })

@login_required
def order_list(request):
    orders = Orders.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Orders, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})