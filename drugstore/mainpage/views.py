from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect
from django.db import models
# from django.db.models.manager import objects

# Create your views here.


def index(request):

    return render(request, 'mainpage/some_html.html', )


def product(request):

    return render(request, 'mainpage/oblozhka.html', )


def poisk(request):

      a = Product.goods.all()
      return render(request, 'mainpage/poisk.html', {"a": a})


