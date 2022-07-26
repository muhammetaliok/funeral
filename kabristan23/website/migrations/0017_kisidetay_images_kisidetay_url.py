# Generated by Django 4.0.3 on 2022-07-27 10:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_remove_kisidetay_images_remove_kisidetay_url'),
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
            field=models.URLField(default=datetime.datetime(2022, 7, 27, 10, 19, 58, 855317, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
