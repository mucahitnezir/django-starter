from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from post.models import Post
from service.models import Service
from portfolio.models import Portfolio
from category.models import Category


class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    i18n = True

    def items(self):
        posts = Post.objects.all()
        return posts

    def lastmod(self, obj):
        return obj.published_at


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    i18n = True

    def items(self):
        categories = Category.objects.filter(type='post')
        return categories

    def lastmod(self, obj):
        return obj.published_at


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    i18n = True

    def items(self):
        services = Service.objects.all()
        return services

    def lastmod(self, obj):
        return obj.published_at


class PortfolioSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    i18n = True

    def items(self):
        portfolios = Portfolio.objects.all()
        return portfolios

    def lastmod(self, obj):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    i18n = True

    def items(self):
        return ['landing:home', 'landing:contact', 'landing:about', 'service:index', 'portfolio:index', 'post:index']

    def location(self, obj):
        return reverse(obj)


sitemaps = {
    'static': StaticViewSitemap,
    'post': PostSitemap,
    'category': CategorySitemap,
    'service': ServiceSitemap,
    'portfolio': PortfolioSitemap,
}
