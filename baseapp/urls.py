"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings

from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.contrib.sitemaps import views as sitemaps_views
from baseapp.sitemaps import sitemaps

from home.views import home_view

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls, name='admin'),
    # Sitemap
    path('sitemap.xml',sitemaps_views.index, {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    path('sitemap-<section>.xml', sitemaps_views.sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
]

urlpatterns += i18n_patterns(
    url(r'^$', home_view, name='home'),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('post.urls')),
    path('accounts/', include('account.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('service/', include('service.urls')),
    prefix_default_language=True
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Change admin site title
admin.site.site_header = "Mücahit Nezir"
admin.site.site_title = "Mücahit Nezir"
