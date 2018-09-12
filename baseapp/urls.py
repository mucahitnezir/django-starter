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
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import home_view

urlpatterns = [
    url(r'^$', home_view, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', include('post.urls')),
    path('accounts/', include('account.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('service/', include('service.urls')),
    path('contact/', include('contact.urls')),
    path('about/', include('about.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Change admin site title
admin.site.site_header = "Mücahit Nezir"
admin.site.site_title = "Mücahit Nezir"
