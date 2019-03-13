from django.urls import path

from .views import ServiceListView, ServiceDetailView

app_name = 'service'

urlpatterns = (
    path('', ServiceListView.as_view(), name='index'),
    path('<slug>/', ServiceDetailView.as_view(), name='detail'),
)
