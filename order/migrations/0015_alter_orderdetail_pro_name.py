# Generated by Django 4.0.4 on 2022-06-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_rename_number_orderdetail_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='pro_name',
            field=models.CharField(max_length=255),
        ),
    ]