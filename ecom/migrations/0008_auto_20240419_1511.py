# Generated by Django 3.0.5 on 2024-04-19 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_product_is_available_product_slug_product_stock_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Query',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
