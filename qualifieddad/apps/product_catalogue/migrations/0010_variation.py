# Generated by Django 2.1 on 2018-10-20 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0009_product_attribute_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='product_catalogue.Attribute')),
                ('attribute_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='product_catalogue.AttributeValue')),
                ('product', models.ManyToManyField(blank=True, related_name='variant', to='product_catalogue.Product')),
            ],
        ),
    ]
