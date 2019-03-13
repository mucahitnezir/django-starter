from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView

from .models import Portfolio
from category.models import Category


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/index.html'
    extra_context = {'title': _('Portfolio')}

    def get_queryset(self):
        return Portfolio.objects.all()

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['categories'] = Category.objects.filter(type='portfolio')
        return data


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Portfolio, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        data['meta_description'] = self.object.short_description
        return data
