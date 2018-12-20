from django.conf.urls import url
from . import views
from django.core.paginator import Paginator
##from django.views.generic import ListView, DetailView
##from .models import product


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product', views.product, name='product'),
    url(r'^poisk', views.poisk, name ='poisk'),
]