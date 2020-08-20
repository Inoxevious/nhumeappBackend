# Generated by Django 3.0.8 on 2020-08-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0027_appmanagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('version_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('app_version', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('app_upload_date', models.DateTimeField()),
                ('app_expire_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'AppVersion',
                'verbose_name_plural': 'AppVersion',
            },
        ),
        migrations.DeleteModel(
            name='AppManagement',
        ),
    ]
