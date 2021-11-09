from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(default='', max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' (' + self.type + ')'
