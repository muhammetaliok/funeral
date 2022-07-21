#from nis import cat
from getpass import getpass
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
##############################################################

def home(request): 
    detay =KisiDetay.objects.all()
    context={'detay':detay}
    return render(request,"front_end/home/index.html",context)

def detay_kisi_create(request):
    form = DetayCreate()
    if request.method == 'POST':
        name=request.POST['name']
        surname=request.POST['surname']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        death_date = request.POST['death_date']
        image = request.POST['image']
        city = request.POST['city']
        adres = request.POST['adres']
        desc = request.POST['desc']
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        KisiDetay.objects.create(name=name,surname=surname,birth_date=birth_date,death_date=death_date,phone_number=phone_number,image=image,city=city,adres=adres,desc=desc,twitter=twitter,facebook=facebook,instagram=instagram)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    getKisi = KisiDetay.objects.all()
    context = {'form':form, 'KisiDetay':getKisi}
    return render(request,"front_end/list/detay_kisi.html",context)    

def list(request): 
    detay =KisiDetay.objects.all()
    context={'detay':detay}
    return render(request, 'front_end/list/index.html',context)

# def list_details(request):
#     detay =KisiDetay.objects.all()
#     context={'detay':detay} 
#     return render(request,"front_end/list/list_details.html",context)

@csrf_exempt
def add_comment(request,slug):
    form = ListComment()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        listComment.objects.create(name=name,email=email,comment=comment)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
    

    detay = KisiDetay.objects.filter(slug=slug)
    if request.method == 'POST':
        name = request.POST.get("name")
        detay.name = name

    getComment = listComment.objects.all()
    userList =userInfo.objects.all()
    context = {'form':form, 'listComment':getComment,'detay':detay,'userList':userList}
    return render(request, 'front_end/list/list_details.html',context)

# def comment_list(request):
#     com_list =listComment.objects.all()
#     context={'com_list':com_list}
#     return render(request, 'front_end/list/list_details.html',context)

 
def search(request): 
    context = {}
    return render(request,"front_end/list/search.html",context)

def blog(request):
    getBlog = blogBilgi.objects.all()
    context = {'getBlog':getBlog}
    return render(request,"front_end/blog/index.html",context)

def blog_details(request,slug): 
    getBlog = blogBilgi.objects.filter(slug = slug)
    if request.method == 'POST':
        blog_title = request.POST.get("blog_title")
        image = request.POST.get("image")
        getBlog.blog_title = blog_title
        getBlog.image = image

    context = {'getBlog':getBlog}
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
        subject = request.POST.get('subject')
        comments = request.POST.get('comments')
        ContactModel.objects.create(name = name,email=email,subject=subject,comments=comments)
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


# def user_info_list(request):
#     userList =userInfo.objects.all()
#     context={'userList':userList}
#     return render(request,"front_end/list/list_details.html",context)

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

def user_comments(request): 
    context = {}
    return render(request,"front_end/user/user-comments.html",context)

def user_approve_comments(request): 
    context = {}
    return render(request,"front_end/user/user-approve-comments.html",context)
    
def user_post_edit(request,): 
    user_id = int(user_id)
    try:
        user_sel = userAddPost.objects.get(id = user_id)
    except userAddPost.DoesNotExist:
        return redirect('website:user-addpost')
    user_form = UserAddPost(request.POST or None, instance = user_sel)
    if user_form.is_valid():
        user_form.save()
        return redirect('website:user-add-post')

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


   