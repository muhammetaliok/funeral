from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import reverse
import sys
from unidecode import unidecode
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tckn = models.CharField(max_length=11, blank=True, null=True)
    slug = models.SlugField(null=True, unique=True, editable=False)
    tel =  models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Müşteri"

    def get_unique_slug(self):
        sayi=0
        slug = slugify(unidecode(self.user.username))
        new_slug=slug
        while Client.objects.filter(slug=new_slug).exists():
            sayi+=1
            new_slug="%s-%s"%(slug,sayi)
        slug = new_slug
        return slug
    def save(self, *args, **kwargs):

        if self.id is None:
            client_username = self.get_unique_slug()
            self.slug = slugify(unidecode(client_username))
        else:
            client=Client.objects.get(slug=self.slug)
            if client.user.username != self.user.username:
                self.slug=self.get_unique_slug()
        super(Client,self).save()

class Duty(models.Model):
    duty_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.duty_name

    class Meta:
        verbose_name_plural = "Kullanıcı Görevi"


class Superadmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    superadmin_duty = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Superadmin"
