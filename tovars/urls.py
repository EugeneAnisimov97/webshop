from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:category_id>/', views.TovarsView.as_view(), name='tovars_list'),
    path('<int:pk>/detail', views.TovarsDetailView.as_view(), name='tovars_detail'),
    path('<int:pk>/update', views.TovarsUpdateView.as_view(), name='tovars_update'),
    path('create/', views.TovarsCreateView.as_view(), name='tovars_create'),
]