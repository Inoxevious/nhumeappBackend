# Generated by Django 3.0.8 on 2020-07-31 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0011_auto_20200731_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
