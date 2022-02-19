# Generated by Django 3.2.3 on 2022-01-17 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
        ('app_shops', '0009_auto_20220110_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='basket',
        ),
        migrations.AlterField(
            model_name='history',
            name='purchase_history',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_history', to='app_shops.ShopsProducts', verbose_name='Продукт в истории покупок'),
        ),
        migrations.CreateModel(
            name='basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents_of_the_basket', models.ManyToManyField(blank=True, null=True, related_name='product_basket', to='app_shops.Products', verbose_name='Продукты в корзине')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.profile', verbose_name='Пользователь')),
            ],
        ),
    ]