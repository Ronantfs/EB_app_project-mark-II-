# Generated by Django 4.1.1 on 2022-09-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EB_app', '0010_rename_order_shippingaddress_examorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='digital',
            field=models.BooleanField(default=False),
        ),
    ]