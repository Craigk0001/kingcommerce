# Generated by Django 2.1 on 2018-10-28 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181028_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_phone', to=settings.AUTH_USER_MODEL),
        ),
    ]
