from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='users_update'),
    path('sign-in/', views.UserCreateView.as_view(), name='users_create'),
]
