# Generated by Django 2.1.5 on 2021-04-13 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_store', '0040_order_shipping_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='appartment_address',
            new_name='s_appartment_address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='s_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='street_address',
            new_name='s_street_address',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zip',
            new_name='s_zip',
        ),
    ]
