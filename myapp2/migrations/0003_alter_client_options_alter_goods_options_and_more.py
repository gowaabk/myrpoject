# Generated by Django 4.2.5 on 2023-10-18 06:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp2", "0002_goods_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "Клиент", "verbose_name_plural": "Клиенты"},
        ),
        migrations.AlterModelOptions(
            name="goods",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="orders",
            options={"verbose_name": "Заказ", "verbose_name_plural": "Заказы"},
        ),
    ]
