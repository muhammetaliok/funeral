# Generated by Django 4.0.3 on 2022-07-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='image',
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_valid_thru',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]