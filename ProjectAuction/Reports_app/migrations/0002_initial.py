# Generated by Django 4.0.5 on 2022-06-18 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reports_app', '0001_initial'),
        ('Auction_app', '0002_initial'),
        ('User_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='successreport',
            name='product_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='User_app.myuser'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.myuser'),
        ),
        migrations.AddField(
            model_name='cancelreport',
            name='auctiondetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='auctionquery',
            name='auctiondetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='auctionquery',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.myuser'),
        ),
    ]
