from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/detail', views.UsersDetailView.as_view(), name='users_detail'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='users_update'),
    path('sign-in/', views.UserCreateView.as_view(), name='users_create'),
]
