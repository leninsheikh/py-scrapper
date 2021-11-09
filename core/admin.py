from django.contrib import admin

from .models import Shop
from .models import Product

admin.site.register(Shop)
admin.site.register(Product)