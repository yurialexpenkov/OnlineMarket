from django.contrib import admin

from app_users.models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',]
    actions = ['mark_as_active', 'mark_as_not_active',]

    def mark_as_active(self, request, queryset):
        queryset.update(status='active user')

    def mark_as_not_active(self, request, queryset):
        queryset.update(status='inactive user')

    mark_as_active.short_description = 'Перевести в статус активный покупатель'
    mark_as_not_active.short_description = 'Перевести в статус неактивный покупатель'

admin.site.register(Profile, ProfileAdmin)