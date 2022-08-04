# Generated by Django 4.0.3 on 2022-07-26 06:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_kisidetay_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisidetay',
            name='images',
            field=models.ImageField(blank=True, upload_to='qrcode'),
        ),
        migrations.AddField(
            model_name='kisidetay',
            name='url',
            field=models.URLField(default=datetime.datetime(2022, 7, 26, 6, 59, 35, 233590, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
