# Generated by Django 3.0.8 on 2020-07-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0008_rides'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='maxWeight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
