# Generated by Django 3.1.7 on 2021-04-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_store', '0023_auto_20210401_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Owner', 'Owner'), ('Admin', 'Admin'), ('User', 'User'), ('', '---')], default='', max_length=5),
        ),
    ]
