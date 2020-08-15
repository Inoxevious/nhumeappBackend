# Generated by Django 3.0.8 on 2020-08-12 07:30

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20200714_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/vendor_images')),
                ('time_update', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TargetMarketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'target_markets_catories',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='vendor_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='procurement',
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCompany', models.CharField(max_length=255)),
                ('nameTrading', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('phoneSales', models.CharField(blank=True, max_length=100, null=True)),
                ('phoneCustomerQueries', models.CharField(blank=True, max_length=100, null=True)),
                ('emailSales', models.CharField(blank=True, max_length=100, null=True)),
                ('emilCustomerQueries', models.CharField(blank=True, max_length=100, null=True)),
                ('mainAddressCity', models.CharField(blank=True, max_length=100, null=True)),
                ('mainAddressResidence', models.CharField(blank=True, max_length=100, null=True)),
                ('mainAddressNeigbhourhood', models.CharField(blank=True, max_length=100, null=True)),
                ('zimraVendorID', models.CharField(blank=True, max_length=100, null=True)),
                ('taxClearance', models.FileField(blank=True, null=True, upload_to='media/vendor_images')),
                ('logoImage', models.ImageField(blank=True, null=True, upload_to='media/vendor_images')),
                ('time_update', models.DateTimeField()),
                ('user', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'vendors',
            },
        ),
        migrations.CreateModel(
            name='TargetMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_categorie', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='products.TargetMarketCategory')),
            ],
            options={
                'verbose_name_plural': 'target_markets',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unqueSellingPoint', models.TextField(blank=True, null=True)),
                ('targetMarket', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/vendor_images')),
                ('time_update', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('vendor_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='products.Vendor')),
            ],
            options={
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='targetMarket',
            field=models.ManyToManyField(to='products.TargetMarket'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Catergory'),
        ),
    ]
