# Generated by Django 4.0.3 on 2022-07-25 11:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogBilgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_date', models.DateField(blank=True, max_length=200, null=True)),
                ('blog_title', models.CharField(blank=True, max_length=150, null=True)),
                ('blog_description', models.CharField(blank=True, max_length=10000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=150, null=True)),
                ('comments', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KisiDetay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('surname', models.CharField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, max_length=200, null=True)),
                ('death_date', models.DateField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('adres', models.CharField(blank=True, max_length=400, null=True)),
                ('desc', models.CharField(blank=True, max_length=10000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='listComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=130, null=True)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('comment_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QrcodeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('get_email', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
            ],
        ),
        migrations.CreateModel(
            name='systemImageBilgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(blank=True, max_length=150, null=True)),
                ('banner_link', models.CharField(blank=True, max_length=150, null=True)),
                ('banner_description', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='userAddPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('il', models.CharField(blank=True, max_length=200, null=True)),
                ('ilce', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('desc', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('desc', models.CharField(blank=True, max_length=400, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldpassword', models.CharField(blank=True, max_length=200, null=True)),
                ('newpassword', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
