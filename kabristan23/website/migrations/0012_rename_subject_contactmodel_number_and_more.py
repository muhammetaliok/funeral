# Generated by Django 4.0.3 on 2022-07-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_payment_card_valid_thru'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='subject',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
