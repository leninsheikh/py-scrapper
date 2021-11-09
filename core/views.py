from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Shop, Product

def index(req):
    products = Product.objects.all()
    context = {'products' : products}
    return render(req, 'core/index.html', context)

def load(req):


    return redirect('/core')



