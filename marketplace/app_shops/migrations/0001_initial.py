# Generated by Django 3.2.3 on 2022-01-03 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название товара')),
                ('price', models.FloatField(default=0, verbose_name='цена')),
                ('price_with_store', models.FloatField(default=0, verbose_name='цена со скидкой')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название магазина')),
                ('store_addresses', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Адреса магазинов')),
                ('product', models.ManyToManyField(blank=True, null=True, related_name='product', to='app_shops.Products', verbose_name='Продукт')),
                ('stock', models.ManyToManyField(blank=True, null=True, related_name='stock', to='app_shops.Products', verbose_name='Акции')),
                ('user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Польователь')),
            ],
            options={
                'verbose_name': 'marketplace',
                'verbose_name_plural': 'marketplace',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_history', models.ManyToManyField(blank=True, null=True, related_name='product_history', to='app_shops.Products', verbose_name='Продукт')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.profile', verbose_name='Пользователь')),
            ],
        ),
    ]