from django.urls import path

from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_index, name='index'),
    path('<slug>/', portfolio_detail, name='detail'),
]
