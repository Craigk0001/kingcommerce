# Generated by Django 2.1 on 2018-10-13 15:48

import apps.product_catalogue.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping', '0001_initial'),
        ('images', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', max_length=250, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('sort_order', models.CharField(choices=[('Name', 'NAME'), ('Priority', 'PRIORITY'), ('Reverse name', 'REVERSE_NAME')], default='Name', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', max_length=250, unique=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_value', to='product_catalogue.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.product_catalogue.models.category_upload_location)),
                ('slug', models.SlugField(help_text='A "slug" is a unique URL-friendly title for an object.', max_length=250, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_category', to='product_catalogue.Category')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_post', to='images.Image')),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('staff_name', models.CharField(max_length=64, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('variations', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('regular_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight_unit', models.CharField(blank=True, max_length=64, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SKU', models.CharField(blank=True, max_length=64, null=True)),
                ('is_donation', models.BooleanField(default=False)),
                ('external_link', models.CharField(blank=True, max_length=64, null=True)),
                ('external_link_text', models.CharField(blank=True, max_length=64, null=True)),
                ('external_link_target', models.CharField(choices=[('New Tab', 'New Tab'), ('New Window', 'New Window'), ('Direct', 'Direct')], default='New Tab', max_length=200)),
                ('engraved', models.BooleanField(default=False)),
                ('can_have_images', models.BooleanField(default=False)),
                ('back_orders', models.CharField(choices=[('Allow', 'Allow'), ('Do not allow', 'Do not allow'), ('Allow, but notify customer', 'Allow, but notify customer')], default='Allow', max_length=200)),
                ('parent_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_product', to='product_catalogue.Product')),
                ('product_image', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='images.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('merchant_notes', models.CharField(blank=True, max_length=800, null=True)),
                ('enable_comments', models.BooleanField(default=False)),
                ('enable_reviews', models.BooleanField(default=False)),
                ('google_prohibited', models.BooleanField(default=False)),
                ('additional', models.CharField(blank=True, max_length=1000, null=True)),
                ('staff_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Pending Review', 'Pending Review'), ('Discontinued', 'Discontinued')], default='Active', max_length=200)),
                ('visibility', models.CharField(choices=[('Public', 'Public'), ('Password Protected', 'Password Protected')], default='Public', max_length=200)),
                ('product_images', models.ManyToManyField(blank=True, related_name='product_post', through='product_catalogue.GalleryImage', to='images.Image')),
                ('shipping_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shipping.ShippingMethod')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('detail', models.CharField(blank=True, max_length=600, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('verified', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewHelpfulness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helpful', models.BooleanField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='product_catalogue.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_value', to='product_catalogue.Options')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='help',
            field=models.ManyToManyField(blank=True, related_name='review_helpful', through='product_catalogue.ReviewHelpfulness', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='product_catalogue.ProductPost'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_image', to='product_catalogue.ProductPost'),
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='product_category', to='product_catalogue.ProductPost'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='attribute', to='product_catalogue.Product'),
        ),
    ]
