from django.urls import path
from django.utils.translation import ugettext_lazy as _

from .views import HomeView, ContactView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path(_('contact/'), ContactView.as_view(), name='contact')
)
