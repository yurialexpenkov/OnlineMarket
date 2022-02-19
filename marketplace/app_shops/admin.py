from django.contrib import admin
from app_shops.models import Shops, Products, History
from django.contrib.auth.models import User

from app_shops.models import Marketplace, ShopsProducts, Basket


class ShopsAdmin(admin.ModelAdmin):
    list_display = ['title', 'store_addresse']

class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ['title', ]

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

class HistoryAdmin(admin.ModelAdmin):
    pass

class ShopsProductsAdmin(admin.ModelAdmin):
    pass

class BasketAdmin(admin.ModelAdmin):
    pass



admin.site.register(Shops, ShopsAdmin)
admin.site.register(Marketplace, MarketplaceAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(ShopsProducts, ShopsProductsAdmin)
admin.site.register(Basket, BasketAdmin)


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['title', 'date', 'activity', 'status']
#     list_filter = ['activity']
#     inlines = [MyCommentInline]
#
#     actions = ['mark_as_active', 'mark_as_not_active', 'translate_the_flag_to_the_truth', 'translate_the_flag_to_false']
#
#     def mark_as_active(self, request, queryset):
#         queryset.update(status='a')
#
#     def mark_as_not_active(self, request, queryset):
#         queryset.update(status='n')
#
#     def translate_the_flag_to_the_truth(self, request, queryset):
#         queryset.update(activity=True)
#
#     def translate_the_flag_to_false(self, request, queryset):
#         queryset.update(activity=False)
#
#
#     mark_as_active.short_description = 'Перевести в статус активно'
#     mark_as_not_active.short_description = 'Перевести в статус неактивно'
