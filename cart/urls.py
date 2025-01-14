from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:tovar_id>/', views.add_to_cart, name='cart_add'),
    path('increase/<int:tovar_id>/', views.cart_add_quantity, name='cart_add_quantity'),
    path('decrease/<int:tovar_id>/', views.cart_reduce_quantity, name='cart_reduce_quantity'),
    path('remove/<int:tovar_id>/', views.cart_remove, name='cart_remove'),
]