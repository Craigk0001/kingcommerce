# Generated by Django 2.1 on 2018-10-19 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0007_auto_20181014_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='product',
            new_name='product_post',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='product',
            new_name='product_post',
        ),
    ]
