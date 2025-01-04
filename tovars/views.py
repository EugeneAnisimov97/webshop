from .models import Tovars, Shop
from django.views.generic import DetailView, ListView
from django.utils.translation import gettext_lazy as _


# Create your views here.
class TovarsView(ListView):
    template_name = 'tovars/tovars_list.html'
    model = Tovars
    context_object_name = 'tovars'
    
    def get_queryset(self):
        shop_id = self.kwargs['shop_id']  # Получаем shop_id из параметров URL
        return Tovars.objects.filter(category__id=shop_id)  # Возвращаем только товары в данной категории
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = Shop.objects.get(id=self.kwargs['shop_id'])  # Получаем магазин из параметров URL
        return context


class TovarsDetailView(DetailView):
    template_name = 'tovars/tovars_detail.html'
    model = Tovars