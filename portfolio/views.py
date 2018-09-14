from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from .models import Portfolio
from category.models import Category


def portfolio_index(request):
    context = {
        'title': _('Portfolio'),
        'portfolios': Portfolio.objects.all(),
        'categories': Category.objects.filter(type='portfolio')
    }
    return render(request, 'portfolio/index.html', context)


def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    context = {
        'title': portfolio.title,
        'meta_description': portfolio.short_description,
        'portfolio': portfolio
    }
    return render(request, 'portfolio/detail.html', context)
