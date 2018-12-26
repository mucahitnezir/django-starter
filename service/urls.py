from django.urls import path

from .views import *

app_name = 'service'

urlpatterns = [
    path('', service_index, name='index'),
    path('<slug>/', service_detail, name='detail'),
]
