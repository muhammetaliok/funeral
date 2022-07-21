from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import Client, Superadmin, Duty
from captcha.fields import ReCaptchaField
import re

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type':'email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adı'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadı'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola Tekrar'}))

    class Meta:
        model = User
        fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adı'}))
    last_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadı'}))
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type':'email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))

    class Meta:
        model = User
        fields=('first_name','last_name','email', 'username', 'password')


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'}))
    #captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('username','password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Hatalı Giriş')

class UserPasswordChangeForm(forms.Form):
    user = None
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Eski Şifre'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre'}))
    new_password_again = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre Tekrar'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_again = self.cleaned_data.get('new_password_again')

        if new_password != new_password_again:
            self.add_error('new_password', 'Yeni Şifreler Eşleşmedi')
            self.add_error('new_password_again', 'Yeni Şifreler Eşleşmedi')

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Lütfen Şifrenizi Giriniz')
        return old_password


class ClientRegisterForm(forms.ModelForm):
    tckn = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control','id':'tckn', 'placeholder': 'Müşteri TC Kimlik No', 'onkeypress':'if ( isNaN( String.fromCharCode(event.keyCode) )) return false;' , 'maxLength':11, 'oninput':'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);'}))
    class Meta:
        model = Client
        fields = ('tckn',)

class SuperadminRegisterForm(forms.ModelForm):
    superadmin_duty = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Çalışanın Görevi'}))
    class Meta:
        model = Superadmin
        fields = ('superadmin_duty','user')

class DutyForm(forms.ModelForm):
    duty_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Görevi'}))
    class Meta:
        model = Duty
        fields = ('duty_name',)

class UpdateClientForm(forms.ModelForm):
    tckn = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'onkeypress':'if ( isNaN( String.fromCharCode(event.keyCode) )) return false;', 'maxLength':11, 'oninput':'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);'}))
    class Meta:
        model = Client
        fields = ['tckn']

class UpdateUserInfoForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'email'}))
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control' ,'readonly':'true'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

# class AboutForm(forms.ModelForm):
#     about_context = RichTextUploadingField(null=True,blank=True)
#     class Meta:
#         model = About
#         fields = ['context','about_footer']
