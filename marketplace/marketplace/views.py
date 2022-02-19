from django.db.models import Max, Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from app_shops.models import History
from app_shops.forms import ForRatingForm


# class MainView(View):

def get_rating(request,):
    if request.method == 'GET':
        products_dict = dict()
        products_all = History.objects.all()
        for products in products_all:
            for single_products in products.purchase_history.all():
                if single_products.product not in products_dict:
                    products_dict[single_products.product.title] = single_products.product.number_of_sales
        products_tuples = sorted(products_dict.items(), key=lambda item: item[1], reverse=True)
        products_dict = {k: v for k, v in products_tuples}
    if request.method == 'POST':
        products_dict = dict()
        products_dict.clear()
        form = ForRatingForm(request.POST)
        if form.is_valid():
            calendar = form.cleaned_data["calendar"]
        products_all = History.objects.all()
        for products in products_all:
            if products.date_of_purchase >= calendar:
                print(products.date_of_purchase, calendar, products.date_of_purchase >= calendar)
                for single_products in products.purchase_history.all():
                    if single_products.product.title not in products_dict:
                        products_dict[single_products.product.title] = 1
                    else:
                        print('попал')
                        products_dict[single_products.product.title] += 1
        print(products_dict)
        products_tuples = sorted(products_dict.items(), key=lambda item: item[1], reverse=True)
        products_dict = {k: v for k, v in products_tuples}
        print(products_dict)
    return render(request, 'main.html', context={'products': products_dict})




