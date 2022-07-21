

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .forms import UserRegisterForm, ClientRegisterForm, SuperadminRegisterForm, LoginForm, UserUpdateForm,UserPasswordChangeForm, DutyForm
from .models import Client, Superadmin, Duty




# Create your views here.




@login_required(login_url='accounts:login')
def admin_home(request):
    nbar="admin_home"
    context = {"nbar":nbar}
    return render(request,"back_end/home/index.html",context)


def get_auth(request):
    flag = False
    gidilecek_sayfa = ""
    if not request.user.is_authenticated:
        flag = True
        gidilecek_sayfa = 'accounts:login'
    try:
        musteri = request.user.clientfatih
        flag = True
        gidilecek_sayfa = 'accounts:home'
    except Exception as e:
        pass
    return flag, gidilecek_sayfa




def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def login_view(request):
    if request.user.is_authenticated:
        try:
            superadmin = request.user.superadmin

            return redirect('accounts:login"')
        except Exception as e:
            pass
        try:
            musteri = request.user.client
            return redirect('accounts:client-login')
        except Exception as e:
            pass

    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user1 = authenticate(username=username, password=password)
            if user1:

                        superadmin = user1.superadmin
                        login(request, user1)
                        messages.success(request, 'Giriş İşlemi Başarılı')
                        return redirect('website:admin_home')
                    # except:
                    #     client = user1.client
                    #     login(request, user1)
                    #     return redirect('website:home')

            else:
                messages.error(request, 'Giriş İşlemi Başarısız')
        else:
            messages.error(request, 'Giriş İşlemi Başarısız')
    else:
        login_form = LoginForm()



    context = {'login_form': login_form,}
    return render(request, 'front_end/accounts/login/login.html', context)


def superadmin_add(request):
    form = SuperadminRegisterForm()
    if request.method == 'POST':
        form = SuperadminRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user']
            form.save()
            super_admin = Superadmin.objects.get(user=username)
            BlogPreview.objects.create(user=super_admin)
    context = {'form':form}
    return render(request,"back_end/superadmin/add_super_admin.html",context)
