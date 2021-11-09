from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse
import logging
import requests
from bs4 import BeautifulSoup
from .models import Shop, Product
from django.utils import timezone

def index(req):
    products = Product.objects.all()
    context = {'products' : products}
    return render(req, 'core/index.html', context)

def load(req):
    page = requests.get("https://www.startech.com.bd/laptop-notebook/laptop?limit=1000")
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.select('.p-item')

    shop = Shop.objects.get(id=1)
    products = []

    for item in items:
        products.append(Product(
            type='laptop',
            shop=shop,
            name=item.select_one('.p-item-name').get_text(),
            price=item.select_one('.p-item-price').get_text())
        )
    
    Product.objects.bulk_create(products)

    return redirect('/core')


