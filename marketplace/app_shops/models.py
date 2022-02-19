from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from app_users.models import Profile

class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Название товара'))
    price = models.FloatField(verbose_name='цена', default=0)
    number_of_sales = models.IntegerField(verbose_name='Количество продаж', default=0)

    def __str__(self):
        return self.title

class Shops(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Название'))
    store_addresse = models.CharField(max_length=1000, blank=True, null=True, verbose_name=_('Адрес магазин'))
    product = models.ManyToManyField(Products, through='ShopsProducts')

    def __str__(self):
        return self.title

class ShopsProducts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество товаров', default=0)

    def __str__(self):
        return f'{self.product.title}, {self.shop.title}'


class Basket(models.Model):
    contents_of_the_basket = models.ManyToManyField(ShopsProducts, related_name='product_basket', blank=True, null=True, verbose_name='Продукты в корзине')
    user = models.ForeignKey(Profile, default=None, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.contents_of_the_basket}'


class History(models.Model):
    purchase_history = models.ManyToManyField(ShopsProducts, related_name='product_history', blank=True, null=True, verbose_name='Продукт в истории покупок')
    user = models.ForeignKey(Profile, default=None, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_purchase = models.DateField(verbose_name='Дата совершения покупки', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.purchase_history}, {self.date_of_purchase}'



class Marketplace(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Название'))
    shop = models.ManyToManyField(Shops, related_name='shop_marketplace', blank=True, null=True, verbose_name=_('Магазин'))
    user = models.ManyToManyField(User, blank=True, null=True, verbose_name=_('Пользователь'))


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('marketplace')
        verbose_name = _('marketplace')



