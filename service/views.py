from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView

from category.models import Category
from .models import Service


class ServiceListView(ListView):
    model = Category
    template_name = 'service/index.html'
    extra_context = {'title': _('Services')}

    def get_queryset(self):
        return Category.objects.filter(type='service')


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Service, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        data['meta_description'] = self.object.meta_description
        return data
