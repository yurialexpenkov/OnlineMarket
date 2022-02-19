from django.urls import path
# from app_shops.views import
from app_shops.views import ProductsListView, ProductsDetailView, buy, addresses, my_basket


urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductsDetailView.as_view()),
    path('products/<int:pk>/basket/', my_basket, name='my_basket'),
    path('products/buy/', buy, name='buy'),
    path('addresses/', addresses, name='addresses'),
]
