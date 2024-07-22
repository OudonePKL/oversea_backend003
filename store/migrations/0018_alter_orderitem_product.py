# Generated by Django 5.0.2 on 2024-04-09 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0017_storemodel_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="orderitem",
                to="store.goodsmodel",
            ),
        ),
    ]