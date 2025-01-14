from .models import Tovars, Category
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.utils.translation import gettext_lazy as _
from .forms import TovarForm
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.
class TovarsView(ListView):
    template_name = 'tovars/tovars_list.html'
    model = Tovars
    context_object_name = 'tovars'
    
    def get_queryset(self):
        category_id = self.kwargs['category_id']  # Получаем shop_id из параметров URL
        return Tovars.objects.filter(category__id=category_id)  # Возвращаем только товары в данной категории
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(id=self.kwargs['category_id'])  # Получаем магазин из параметров URL
        return context


class TovarsDetailView(DetailView):
    template_name = 'tovars/tovars_detail.html'
    model = Tovars


class TovarsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Tovars
    form_class = TovarForm
    success_url = reverse_lazy('index')
    success_message = _('Tovar successfully created')
    extra_context = {
        'head': _('Create tovar'),
        'button_text': _('Create'),
    }

class TovarsUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Tovars
    form_class = TovarForm
    success_url = reverse_lazy('index')
    success_message = _('Tovar successfully modified')
    extra_context = {
        'head': _('Change tovar'),
        'button_text': _('Change'),
    }