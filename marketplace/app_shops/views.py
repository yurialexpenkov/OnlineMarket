from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.core.cache import cache
import random
from app_shops.models import Shops, Products, History
from app_users.models import Profile
from app_shops.models import ShopsProducts, Basket
from app_shops.forms import ToBusketForm

def random_number():
    return random.randint(1, 100)


class ProductsListView(generic.ListView):
    model = Products
    template_name = 'marketplace/products_list.html'
    context_object_name = 'products_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = ShopsProducts.objects.all()
        context['rand'] = random_number()
        return context


class ProductsDetailView(generic.DetailView):
    model = Products
    template_name = 'marketplace/products_detail.html'

def my_basket(request, pk,):
    if request.method == 'POST':
        post_id = cache.get('post_id')
        print(post_id)
        form = ToBusketForm(request.POST)
        if form.is_valid():
            shop_id = form.cleaned_data["shop_id"]
            print(form.cleaned_data['post_id'])
            if post_id == form.cleaned_data['post_id']:
                print('Попал')
                return HttpResponseRedirect('/marketplace/products/')
            post_id = form.cleaned_data['post_id']
            cache.set('post_id', post_id)
            print(post_id)
        user_id = request.user.id
        profile = Profile.objects.get(user_id=user_id)
        product = Products.objects.get(pk=pk)
        poduct_for_basket = ShopsProducts.objects.filter(product=product)
        for poduct in poduct_for_basket:
            # if 2 > 1:
            if poduct.shop.id == shop_id:
                if poduct.quantity > 0:
                    basket = Basket.objects.create(user=profile)
                    basket.contents_of_the_basket.add(poduct)
                    basket.save()
                    basket = Basket.objects.filter(user_id=user_id)
                else:
                    return HttpResponseRedirect('/marketplace/products/')
    rand = random.randint(1, 1000)
    return render(request, 'marketplace/my_basket.html', context={'basket': basket, 'rand': rand})


def buy(request):
    if request.method == 'POST':
        user_id = request.user.id
        profile = Profile.objects.get(user_id=user_id)
        history = History.objects.create(user=profile)
        basket = Basket.objects.filter(user=user_id)
        for record in basket.all():
            for product in record.contents_of_the_basket.all():
                if profile.balance >= product.product.price:
                    profile.balance -= product.product.price
                    profile.status = 'active user'
                    profile.save()
                    product.product.number_of_sales = product.product.number_of_sales + 1
                    product.product.save(update_fields=['number_of_sales'])
                    product.quantity -= 1
                    product.save(update_fields=['quantity'])
                    history.purchase_history.add(product)
                    history.save()
                    record.delete()
                    record.save()
                else:
                    return HttpResponseRedirect(f'/marketplace/products/')
        return HttpResponseRedirect(f'/marketplace/products/')


def addresses(request):
    shop = Shops.objects.first()
    addresses = shop.store_addresses
    print(addresses)
    return render(request, 'marketplace/addresses.html', context={'addresses': addresses})

