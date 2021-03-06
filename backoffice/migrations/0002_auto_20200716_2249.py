# Generated by Django 3.0.8 on 2020-07-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddressEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryAddressId', models.CharField(blank=True, max_length=100, null=True)),
                ('isPrimary', models.BooleanField(default=True)),
                ('postalCode', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('unitNumber', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurantName', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('unitNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=100, null=True)),
                ('isOperating', models.BooleanField(default=True)),
                ('rating', models.CharField(blank=True, max_length=100, null=True)),
                ('cuisineType', models.CharField(blank=True, max_length=100, null=True)),
                ('foodPreferences', models.CharField(blank=True, max_length=100, null=True)),
                ('menuEntities', models.CharField(blank=True, max_length=100, null=True)),
                ('reviewEntities', models.CharField(blank=True, max_length=100, null=True)),
                ('imagePath', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLineItemEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionLineItemId', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('serialNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('unitPrice', models.CharField(blank=True, max_length=100, null=True)),
                ('subTotal', models.CharField(blank=True, max_length=100, null=True)),
                ('menuItemEntity', models.CharField(blank=True, max_length=100, null=True)),
                ('customisableItemId', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='customisableItemEntities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='customisableItemId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='foodItemEntities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='menuItemEntity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='isRider',
            field=models.BooleanField(default=True),
        ),
    ]
