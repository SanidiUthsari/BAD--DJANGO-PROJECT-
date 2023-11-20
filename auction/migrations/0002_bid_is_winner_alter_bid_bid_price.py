# Generated by Django 4.2.7 on 2023-11-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="is_winner",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="bid",
            name="bid_price",
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]