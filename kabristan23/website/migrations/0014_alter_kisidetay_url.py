# Generated by Django 4.0.3 on 2022-07-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_kisidetay_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisidetay',
            name='url',
            field=models.URLField(),
        ),
    ]