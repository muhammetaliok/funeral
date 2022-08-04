from string import capwords
from tkinter import Widget
from xml.etree.ElementTree import Comment
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

        
class DetayCreate(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İsminiz'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Soy İsminiz'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Doğum Tarihiniz' ,'required': 'required' , 'rows':6,}))
    death_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Ölüm Tarihiniz' ,'required': 'required' , 'rows':6,}))
    email = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'mail'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Numaranız'}))
    image = forms.ImageField()
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Şehir'}))
    adres = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Adresiniz'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Açıklama'}))
    slug = forms.SlugField( )
    twitter = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'twitter'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'facebook'}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'instagram'}))

    class Meta:
        model = KisiDetay
        fields = ['name','surname','birth_date','email','death_date','phone_number','image','city','adres','desc','slug','twitter','facebook','instagram']

    def clean(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            surname = self.cleaned_data['surname']
            birth_date = self.cleaned_data['birth_date']
            death_date = self.cleaned_data['death_date']
            phone_number = self.cleaned_data['phone_number']
            image = self.cleaned_data['image']
            city = self.cleaned_data['city']
            adres = self.cleaned_data['adres']
            desc = self.cleaned_data['desc']
            twitter = self.cleaned_data['twitter']
            facebook = self.cleaned_data['facebook']
            instagram = self.cleaned_data['instagram']


        
class blogForm(forms.ModelForm):
    blog_title = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Blog Başlık'}))
    blog_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Blog Tarihi' ,'required': 'required' , 'rows':6,}))
    blog_description = forms.CharField(max_length=100000,widget=CKEditorWidget(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Blog Açıklama' ,'required': 'required' , 'rows':6,}))
    image = forms.ImageField()
    slug = forms.SlugField( )
    category = forms.ModelChoiceField(queryset=BlogCategory.objects.all(),widget=forms.Select(attrs={'class':'selectpicker form-control ', 'data-live-search':'true',}))
    class Meta:
        model = blogBilgi
        fields = ['blog_title','blog_date','blog_description','image','category']


class contactForm(forms.ModelForm):
    name = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'name'}))
    email = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'mail'}))
    subjects = forms.CharField(max_length=550, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'subject'}))
    comments = forms.CharField(max_length=100000,widget=CKEditorWidget(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'message' ,'required': 'required' , 'rows':6,}))
    class Meta:
        model = ContactModel
        fields = ['name','email','subjects','comments']

class UserInfo(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İsminiz'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Numaranız'}))
    image = forms.ImageField()
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'email'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Açıklama'}))
    twitter = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'twitter'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'facebook'}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'instagram'}))

    class Meta:
        model = userInfo
        fields = ['name','phone_number','image','email','desc','twitter','facebook','instagram']

    def clean(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            phone_number = self.cleaned_data['phone_number']
            image = self.cleaned_data['image']
            email = self.cleaned_data['email']
            desc = self.cleaned_data['desc']
            twitter = self.cleaned_data['twitter']
            facebook = self.cleaned_data['facebook']
            instagram = self.cleaned_data['instagram']

class UserAddPost(forms.ModelForm):
    image = forms.ImageField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İsminiz'}))
    il = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İl'}))
    ilce = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'İlçe'}))
    desc =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Açıklama'}))
    

    class Meta:
        model = userAddPost
        fields = ['image','name','il','ilce','desc']

    def clean(self):
        if self.is_valid():
            image = self.cleaned_data['image']
            name = self.cleaned_data['name']
            il = self.cleaned_data['il']
            ilce = self.cleaned_data['ilce']
            desc = self.cleaned_data['desc']

class UserPassword(forms.ModelForm):
    oldpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded-0','autocomplete':'off',}))
    newpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded-0','autocomplete':'off',}))
    
    class Meta:
        model = userPassword
        fields = ['oldpassword','newpassword']

class ListComment(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off'}))
    email = forms.ChoiceField(widget=forms.EmailInput(attrs={'class':'form-control rounded-0','autocomplete':'off'}))
    comment = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off'}))
    comment_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control rounded-0 w-100','required': 'required' }))
    class Meta:
        model = listComment
        fields = ['name','email','comment','comment_date']
    
class Payment(forms.ModelForm):
    cardholder_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off'}))
    card_cvv = forms.IntegerField()
    card_valid_thru = forms.IntegerField()

    class Meta:
        model = payment
        fields = ['cardholder_name','card_number','card_cvv','card_valid_thru']

class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Kitap Adı'}))
    author= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control rounded-0','autocomplete':'off', 'placeholder': 'Yazar'}))
    description = forms.CharField(max_length=100000,widget=CKEditorWidget(attrs={'class':'form-control rounded-0 w-100', 'placeholder': 'Hizmet Açıklama İngilizce' ,'required': 'required' , 'rows':6,}))
    
    class Meta:
        model = Book
        fields = ['name','author','description']