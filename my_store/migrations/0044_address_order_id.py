# Generated by Django 2.1.5 on 2021-04-13 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_store', '0043_auto_20210413_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_store.Order'),
        ),
    ]