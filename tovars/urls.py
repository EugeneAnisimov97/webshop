from django.urls import path
from . import views

urlpatterns = [
    path('<int:shop_id>/', views.TovarsView.as_view(), name='tovars_list'),
    path('<int:shop_id>/detail', views.TovarsDetailView.as_view(), name='tovars_detail'),
]
