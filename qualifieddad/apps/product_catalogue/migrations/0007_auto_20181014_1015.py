# Generated by Django 2.1 on 2018-10-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0006_auto_20181014_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='attribute', to='product_catalogue.ProductPost'),
        ),
    ]