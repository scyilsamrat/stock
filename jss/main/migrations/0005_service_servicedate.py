# Generated by Django 4.1 on 2022-09-01 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_parts_service_delete_customer_delete_invoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='servicedate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
