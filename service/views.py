from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Service


def service_index(request):
    context = {
        'title': 'Hizmet Listesi',
        'categories': Category.objects.filter(type='service')
    }
    return render(request, 'service/index.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {
        'service': service
    }
    return render(request, 'service/detail.html', context)
