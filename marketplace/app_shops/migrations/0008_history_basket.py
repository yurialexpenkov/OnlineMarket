# Generated by Django 3.2.3 on 2022-01-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0007_remove_products_price_with_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='basket',
            field=models.ManyToManyField(blank=True, null=True, related_name='basket', to='app_shops.Products', verbose_name='Продукт'),
        ),
    ]