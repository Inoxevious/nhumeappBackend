# Generated by Django 3.0.8 on 2020-07-31 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0013_auto_20200731_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='package_user',
            new_name='packageOwner',
        ),
    ]
