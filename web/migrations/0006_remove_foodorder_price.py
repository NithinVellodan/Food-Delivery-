# Generated by Django 4.1.7 on 2023-04-29 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_foodorder_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodorder',
            name='price',
        ),
    ]