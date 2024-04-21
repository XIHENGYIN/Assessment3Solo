# Generated by Django 4.1 on 2024-04-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_rename_sell_price_product_original_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
