import email
from statistics import mode

from unicodedata import category, name
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

from ckeditor.fields import RichTextField
from unidecode import unidecode
from django.utils.text import slugify
import datetime
import random


class systemImageBilgi(models.Model):
    banner_title = models.CharField(max_length = 150, null=True, blank=True)
    banner_link = models.CharField(max_length = 150, null=True, blank=True)
    banner_description = RichTextField(max_length = 1000, null=True, blank=True) 
    image = models.ImageField(null = False,blank=True)
    class Meta:
        verbose_name_plural = "Slider"
    def __str__(self):
          return self.banner_title+ " - " + self.banner_link+ " - " + self.banner_description+ " - "




class KisiDetay(models.Model):
    url=models.URLField(max_length = 200)
    name = models.CharField(max_length=200,blank=True,null=True)
    surname = models.CharField(max_length=200,blank=True,null=True)
    birth_date = models.DateField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    death_date = models.DateField(max_length=200,blank=True,null=True)
    phone_number = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(null = False ,blank=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    adres = models.CharField(max_length=400,blank=True,null=True)
    desc = models.CharField(max_length=10000,null=True,blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True,null=True)
    twitter = models.CharField(max_length=50,blank=True,null=True)
    facebook = models.CharField(max_length=50,blank=True,null=True)
    instagram = models.CharField(max_length=50,blank=True,null=True)
    images = models.ImageField(upload_to='qrcode',blank=True)

    def __str__(self):
        return self.name 

    @property
    def get_image_or_default(self):
       if self.images and hasattr(self.images, 'url'):
           return self.images.url
       return '/media/category_image/default_image/default.webp'

    def get_unique_slug(self):
        sayi=0
        slug = slugify(unidecode(self.name))
        new_slug=slug
        while KisiDetay.objects.filter(slug=new_slug).exists():
            sayi+=1
            new_slug="%s-%s"%(slug,sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            name = self.get_unique_slug()
            self.slug = slugify(unidecode(name))
        else:
            blog=KisiDetay.objects.get(slug=self.slug)
            if blog.name != self.name:
                self.slug=self.get_unique_slug()
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.images.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()

        super(KisiDetay,self).save()
    
       


class BlogCategory(models.Model):
    name = models.CharField(max_length = 250,null=True,blank=True)
    def __str__(self):
        return self.name


class blogBilgi(models.Model):
    blog_date = models.DateField(max_length=200,blank=True,null=True)
    blog_title = models.CharField(max_length = 150, null=True, blank=True)
    blog_description = models.CharField(max_length = 10000, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True,null=True)
    image = models.ImageField(null = False,blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.blog_title 

    def get_unique_slug(self):
        sayi=0
        slug = slugify(unidecode(self.blog_title))
        new_slug=slug
        while blogBilgi.objects.filter(slug=new_slug).exists():
            sayi+=1
            new_slug="%s-%s"%(slug,sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            blog_title = self.get_unique_slug()
            self.slug = slugify(unidecode(blog_title))
        else:
            blog=blogBilgi.objects.get(slug=self.slug)
            if blog.blog_title != self.blog_title:
                self.slug=self.get_unique_slug()
        super(blogBilgi,self).save()

class ContactModel(models.Model):
    name = models.CharField(max_length = 150, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    subjects = models.CharField(max_length = 150, null=True, blank=True)
    comments = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class userAddPost(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    il = models.CharField(max_length=200,blank=True,null=True)
    ilce = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(null = False ,blank=True)
    desc = models.CharField(max_length=10000,blank=True,null=True)

    def __str__(self):
        return self.name

class userPassword(models.Model):
    oldpassword = models.CharField(max_length=200,blank=True,null=True)
    newpassword = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.newpassword

class listComment(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=130,null=True,blank=True)
    comment = models.TextField(max_length=1000,null=True,blank=True)
    comment_date = models.DateTimeField(null=True,blank=True)
    is_valid = models.BooleanField(default=0)

    def __str__(self):
        return self.name

#class payment (models.Model):
#    card_cvv = models.CharField(max_length=3,blank=True,null=True)
#    card_valid_thru = models.CharField(max_length=7,blank=True,null=True)
#    cardholder_name = models.CharField(max_length=200,blank=True,null=True)
#    card_number = models.CharField(max_length=30,blank=True,null=True)

#    def _str_(self):
#        return self.cardholder_name
