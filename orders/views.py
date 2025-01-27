from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Orders, OrderItem
from tovars.models import Tovars
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView, DetailView, ListView
)
from django.urls import reverse_lazy
from .forms import OrderForm
from django.utils.translation import gettext_lazy as _
from django.views import View
from webshop.mixins import get_cart, CheckLoginMixin

class CreateOrderView(CheckLoginMixin, View):
    template_name = 'orders/order_create.html'

    def get(self, request):
        cart = get_cart(request)
        tovars = []
        total_amount = 0 
        for tovar_id, quantity in cart.items():
            tovar = get_object_or_404(Tovars, id=tovar_id)
            tovars.append((tovar, quantity))
            total_amount += tovar.price * quantity

        address = request.user.address
        phone = request.user.phone 

        return render(request, self.template_name, {
            'tovars': tovars,
            'address': address,
            'phone': phone,
            'cart': cart,
            'total_amount': total_amount
        })

    def post(self, request):
        cart = get_cart(request)
        if not cart:
            messages.error(request, "Корзина пуста!")
            return redirect('cart_detail')
        order = Orders.objects.create(
            user=request.user,
            total_amount=0,  # Общая сумма будет обновлена позже
            address=request.POST.get('address', request.user.address),
            phone=request.POST.get('phone', request.user.phone)
        )
        total_amount = 0
        
        # Создаем заказ для каждого товара в корзине
        for tovar_id, quantity in cart.items():
            tovar = get_object_or_404(Tovars, id=tovar_id)
            price = tovar.price

            # Создаем элемент заказа
            order_item = OrderItem.objects.create(
                order=order,
                tovar=tovar,
                quantity=quantity,
                price=price
            )
            # Уменьшаем количество товара на складе
            tovar.stock -= quantity
            tovar.save()
            
            # Суммируем общую сумму
            total_amount += order_item.price * order_item.quantity

        # Обновляем общую сумму заказа
        order.total_amount = total_amount
        order.save()

        # Очищаем корзину
        self.clear_cart(request)
        
        messages.success(request, "Заказ успешно создан!")
        return redirect('orders_list')
    
    def clear_cart(self, request):
        request.session['cart'] = {}


class OrderDetailView(DetailView):
    template_name = 'orders/order_detail.html'
    model = Orders
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()  # Получаем все товары, связанные с заказом
        return context


class OrderListView(ListView):
    template_name = 'orders/order_list.html'
    model = Orders
    context_object_name = 'orders'