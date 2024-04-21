# Generated by Django 4.1 on 2024-04-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_productprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='ProductPrice',
        ),
    ]
