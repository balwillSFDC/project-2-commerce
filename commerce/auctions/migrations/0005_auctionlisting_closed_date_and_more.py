# Generated by Django 4.0.6 on 2022-07-10 23:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctionlisting_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]