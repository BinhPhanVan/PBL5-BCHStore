# Generated by Django 4.0.4 on 2022-06-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_name_order_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='name_receive',
        ),
    ]