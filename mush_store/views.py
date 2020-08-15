from django.shortcuts import render
from products.models import Product
from django.db.models import Q
from django.conf import settings
import os
from cart.cart import Cart
# Create your views here.
def index(request):
    qs = Product.objects.all()
    new_arrivals = Product.objects.all()[:3]
    promotions  = Product.objects.all()[:3]
    slider = Product.objects.all()[:3]
    context = {"qs":qs,
    "new_arrivals":new_arrivals, "slider":slider, "promotions":promotions
    }


    return render(request,'unify/index.html', context)


def about(request):
    return render(request, 'unify/index.html')

def login(request):
    return render(request, 'unify/lindex.html')

def contact(request):
    return render(request, 'unify/index.html')

def blog_detail(request):
    return render(request, 'unify/index.html')

def product(request):
    return render(request, 'unify/index.html')

def product_detail(request):
    return render(request, 'unify/index.html')

def blog(request):
    return render(request, 'unify/bindex.html')

def cart(request):
    return render(request, 'unify/index.html')

def faq(request):
    return render(request, 'unify/index.html')