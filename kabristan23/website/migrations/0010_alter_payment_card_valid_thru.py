# Generated by Django 4.0.3 on 2022-07-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_payment_email_remove_payment_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_valid_thru',
            field=models.DateField(blank=True, null=True),
        ),
    ]
