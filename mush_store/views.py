from django.shortcuts import render
from products.models import Product
from django.db.models import Q
from django.conf import settings
from backoffice.models import *
import os
import mimetypes
from cart.cart import Cart
# Create your views here.
from django.views import generic

class AppDownloadView(generic.ListView):
    model = AppVersion
    fields = ['file']
    template_name = 'unify/app.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app = AppVersion.objects.all()
        for file in app:
            print('App Data'+file)
        context['object_list'] = AppVersion.objects.all()
        return context


def download_file(request):
    # fill these variables with real values
    queryset = AppVersion.objects.all()
    print("This App"+queryset)
    fl_path = '/file/path'
    filename = 'downloaded_file_name.extension'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

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