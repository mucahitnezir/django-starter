from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from category.models import Category


def portfolio_index(request):
    context = {
        'portfolios': Portfolio.objects.all(),
        'categories': Category.objects.filter(type='portfolio'),
        'title': 'Portfolio'
    }
    return render(request, 'portfolio/index.html', context)


def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    context = {
        'portfolio': portfolio,
        'title': portfolio.title,
        'meta_description': portfolio.short_description
    }
    return render(request, 'portfolio/detail.html', context)
