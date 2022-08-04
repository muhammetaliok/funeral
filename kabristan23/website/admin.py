from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(KisiDetay)
admin.site.register(blogBilgi)
admin.site.register(BlogCategory)
admin.site.register(systemImageBilgi)
admin.site.register(ContactModel)
admin.site.register(userInfo)
admin.site.register(userAddPost)
admin.site.register(userPassword)
admin.site.register(listComment)
admin.site.register(payment)
admin.site.register(Book)


