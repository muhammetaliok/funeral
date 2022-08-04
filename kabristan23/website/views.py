#from nis import cat
from email.policy import default
from getpass import getpass
from inspect import getcomments
from typing import List
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from urllib.parse import urlencode
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm

from django.views import generic
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from qrcode import *

##############################################################

def home(request): 
    detay =KisiDetay.objects.all()
    context={'detay':detay}
    return render(request,"front_end/home/index.html",context)

def detay_kisi_create(request):
    form = DetayCreate()
    if request.method == 'POST':
        url = request.POST.get('url')
        name=request.POST['name']
        surname=request.POST.get('surname')
        phone_number = request.POST['phone_number']
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        death_date = request.POST.get('death_date')
        image = request.POST['image']
        city = request.POST.get('city')
        adres = request.POST.get('adres')
        desc = request.POST.get('desc')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        KisiDetay.objects.create(url="https://twitter.com/home",name=name,surname=surname,email=email,birth_date=birth_date,death_date=death_date,phone_number=phone_number,image=image,city=city,adres=adres,desc=desc,twitter=twitter,facebook=facebook,instagram=instagram)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getKisi = KisiDetay.objects.all()
    context = {'form':form, 'KisiDetay':getKisi}
    return render(request,"front_end/user/detay_kisi.html",context)    

def list(request): 
    detay =KisiDetay.objects.all()
    context={'detay':detay}
    return render(request, 'front_end/list/index.html',context)


@csrf_exempt
def add_comment(request,slug):
    detay = KisiDetay.objects.filter(slug=slug)
    if request.method == 'POST':
        name = request.POST.get("name")
        detay.name = name
    form = ListComment()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        listComment.objects.create(name=name,email=email,comment=comment)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    

    
    getComment = listComment.objects.all()
    userList =userInfo.objects.all()
    context = {'form':form, 'listComment':getComment,'detay':detay,'userList':userList}
    return render(request, 'front_end/list/list_details.html',context)


 
def search(request,name): 
    detay = KisiDetay.objects.filter(city=name)
    context = {'detay':detay}
    return render(request,"front_end/list/search.html",context)

def blog(request):
    getBlog = blogBilgi.objects.all()
    p = Paginator(blogBilgi.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {'getBlog':getBlog,'venues':venues,'p':p}
    return render(request,"front_end/blog/index.html",context)

def blog_details(request,slug): 
    getBlog = blogBilgi.objects.filter(slug = slug)
    if request.method == 'POST':
        blog_title = request.POST.get("blog_title")
        image = request.POST.get("image")
        getBlog.blog_title = blog_title
        getBlog.image = image
    
    
    get_blog = blogBilgi.objects.all()[:3]
    context = {'getBlog':getBlog,'get_blog': get_blog}
    return render(request,"front_end/blog/blog_details.html",context)

def add_blog(request):
    form = blogForm()
    if request.method == 'POST':
        blog_title=request.POST['blog_title']
        blog_date=request.POST['blog_date']
        blog_description = request.POST['blog_description']
        image = request.POST.get('image')
        blogBilgi.objects.create(blog_title=blog_title,blog_date=blog_date,blog_description=blog_description,image=image)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getBlog = blogBilgi.objects.all()
    context = {'form':form, 'blogBilgi':getBlog}
    return render(request,"front_end/user/add_blog.html",context)    


def update_blog(request,id):
    if request.user.is_anonymous:
        return redirect('website:login')
    marka = blogBilgi.objects.get(id = id)
    if request.method == 'POST':
        blog_title = request.POST.get("blog_title")
        blog_date = request.POST.get("blog_date")
        blog_description = request.POST.get("blog_description")
        image = request.FILES["image"]
        blog.blog_title = blog_title
        blog.blog_date = blog_date
        blog.blog_description = blog_description
        blog.image = image
        blog.save()
  
    context = {'blog':blog}
    return render(request,"front_end/blog/update_blog.html",context)

def delete_blog(request):
    id = request.POST.get("delete")
    category = blogBilgi.objects.get(id = id )
    category.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def about(request): 
    context = {}
    return render(request,"front_end/about/index.html",context)

@csrf_exempt
def contact(request):
    # success = False
    form = contactForm()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjects = request.POST.get('subjects')
        comments = request.POST.get('comments')
        ContactModel.objects.create(name = name,email=email,subjects=subjects,comments=comments)
        success = True
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    contact_kisi = ContactModel.objects.all()
    context = {'ContactModel':contact_kisi,'form':form}
    return render(request,"front_end/contact/index.html",context)

@csrf_exempt
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("website:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"back_end/login/register.html", {"register_form":form})

@csrf_exempt
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("website:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"back_end/login/login.html", {"login_form":form})



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("website:login")





def user_info(request): 
    form = UserInfo()
    if request.method == 'POST':
        name=request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        image = request.POST.get('image')
        desc = request.POST['desc']
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')

        userInfo.objects.create(name=name,phone_number=phone_number,email=email,image=image,desc=desc,twitter=twitter,facebook=facebook,instagram=instagram)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getUserInfo = userInfo.objects.all()
    context = {'form':form, 'userInfo':getUserInfo}
    return render(request,"front_end/user/user-info.html",context)   



def user_post(request):
    detay =userAddPost.objects.all()
    context={'detay':detay}
    return render(request,"front_end/user/user-post.html",context)

@csrf_exempt
def user_add_post(request): 
    form = UserAddPost()
    if request.method == 'POST':
        name=request.POST['name']
        il = request.POST['il']
        ilce = request.POST['ilce']
        image = request.POST.get('image')
        desc = request.POST['desc']

        userAddPost.objects.create(name=name,il=il,ilce=ilce,image=image,desc=desc)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getAddUser = userAddPost.objects.all()
    context = {'form':form, 'userAddPost':getAddUser}
    return render(request,"front_end/user/user-add-post.html",context)   


def user_comments(request,id): 
    get_valid = listComment.objects.get(id=id)
    button = request.POST.get("myButton")
    if button:
        get_valid.is_valid = 1
        get_valid.save()
    else:
        print("merhaba")
    context = {'get_valid':get_valid}
    return render(request,"front_end/user/user-comments.html",context)

def user_approve_comments(request): 
    getComment = listComment.objects.all()
    if request.method == 'POST':
        return redirect('front_end/user/user_comments.html')
    
    context = {'getComment':getComment}
    return render(request,"front_end/user/user-approve-comments.html",context)
    



@csrf_exempt
def user_post_edit(request,id):  
    detay = userAddPost.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get("name")
        il = request.POST.get("il")
        ilce = request.POST.get("ilce")
        image = request.FILES.get("image")
        desc = request.POST.get("desc")

        detay.name = name
        detay.il = il
        detay.ilce = ilce
        detay.image = image
        detay.desc = desc
        detay.save()

  
    context = {'detay':detay}
    return render(request,"front_end/user/user-post-edit.html",context)

def user_post_delete(request):
    id = request.POST.get("delete")
    category = UserAddPost.objects.get(id = id)
    category.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def user_password(request): 
    form = UserPassword()
    if request.method == 'POST':
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        
        userPassword.objects.create(oldpassword=oldpassword,newpassword=newpassword)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))

    getPassword = userPassword.objects.all()
    context = {'form':form,'userPassord':getPassword}
    return render(request,"front_end/user/user-password.html",context)



@csrf_exempt
def payment_method(request):
    form = Payment()
    if request.method == 'POST':
        cardholder_name=request.POST['cardholder_name']
        card_cvv = request.POST['card_cvv']
        # email = request.POST['email']
        # image = request.POST.get('image')
        card_number = request.POST['card_number']
        card_valid_thru = request.POST['card_valid_thru']

        payment.objects.create(cardholder_name=cardholder_name,card_cvv=card_cvv,card_number=card_number,card_valid_thru=card_valid_thru)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getPayment = payment.objects.all()
    context = {'form':form,'getPayment':getPayment}
    return render(request,"front_end/payment/payment.html",context)
