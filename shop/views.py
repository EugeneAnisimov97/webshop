from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, CreateView
from . import models
from django_filters.views import FilterView
from .models import Category
from shop.forms import CategoryForm


class IndexView(TemplateView):
    template_name = 'shop/index.html'
    extra_context = {
        'head': _('Categories'),
        'button_text': _('Go'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = models.Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'shop/about.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('index')
    success_message = _("You are logged in")
    extra_context = {
        'head': _('Login'),
        'button_text': _('Login'),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)

class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('index')
    success_message = _('Category successfully created')
    extra_context = {
        'head': _('Create Category'),
        'button_text': _('Create'),
    }