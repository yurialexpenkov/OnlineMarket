# Generated by Django 3.2.3 on 2022-01-18 20:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_shops', '0012_alter_basket_contents_of_the_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplace',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
