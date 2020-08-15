# Generated by Django 3.0.8 on 2020-08-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0018_auto_20200810_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='courierState',
            field=models.CharField(blank=True, choices=[('pickupPoit', 'pickupPoit'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('returning', 'returning'), ('returned', 'returned')], default='pickupPoit', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='currentState',
            field=models.CharField(blank=True, choices=[('biddingOpen', 'Bidding Open'), ('biddingClosed', 'Bidding Closed'), ('biddingSuspended', 'Bidding Suspended'), ('biddingReopened', 'Bidding Reopened')], default='biddingOpen', max_length=100, null=True),
        ),
    ]
