# Generated by Django 4.0.3 on 2022-07-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_listcomment_is_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
