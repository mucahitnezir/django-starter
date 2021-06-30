from django.urls import path
from django.utils.translation import ugettext_lazy as _

from landing.views import HomeView, AboutView, ContactView


app_name = 'landing'

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path(_('about/'), AboutView.as_view(), name='about'),
    path(_('contact/'), ContactView.as_view(), name='contact')
)
