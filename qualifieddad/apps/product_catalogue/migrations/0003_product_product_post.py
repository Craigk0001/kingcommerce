# Generated by Django 2.1 on 2018-10-13 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0002_auto_20181013_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_catalogue.ProductPost'),
        ),
    ]
