# Generated by Django 4.1 on 2022-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_service_servicedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='place',
            field=models.CharField(default='guna', max_length=100),
            preserve_default=False,
        ),
    ]
