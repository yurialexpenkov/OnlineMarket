# Generated by Django 3.2.3 on 2022-01-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('a', 'True'), ('n', 'False')], max_length=1, null=True),
        ),
    ]