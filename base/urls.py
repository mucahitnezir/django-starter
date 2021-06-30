from django.contrib import admin
from django.conf import settings

from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from django.contrib.sitemaps import views as sitemaps_views
from django.views.generic import TemplateView

from .sitemaps import sitemaps

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls, name='admin'),
    # Sitemap
    path('sitemap.xml', sitemaps_views.index, {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    path('sitemap-<section>.xml', sitemaps_views.sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
    # robots.txt
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

urlpatterns += i18n_patterns(
    path('', include('landing.urls')),
    path(_('blog/'), include('post.urls')),
    path(_('accounts/'), include('account.urls')),
    path(_('portfolio/'), include('portfolio.urls')),
    path(_('service/'), include('service.urls')),
    prefix_default_language=True
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Change admin site title
admin.site.site_header = 'Mücahit Nezir'
admin.site.site_title = 'Mücahit Nezir'
