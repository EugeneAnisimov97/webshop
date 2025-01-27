from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='orders_list'), 
    path('create/', views.CreateOrderView.as_view(), name='orders_create'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='orders_detail'),
]