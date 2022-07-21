from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Client
from accounts.views import get_auth
from accounts.forms import UpdateClientForm, UpdateUserInfoForm, UserPasswordChangeForm
from accounts.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

def client_password_change(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    form = UserPasswordChangeForm(user=request.user, data=request.POST or None)
    if request.POST:
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Şifre Güncelleme İşlemi Başarılı')
        else:
            messages.error(request, 'Şifre Güncelleme İşlemi Başarısız.!!')

        return redirect("musteri-panel")

    user = User.objects.filter(pk=request.user.pk)[0]
    userForm = UpdateUserInfoForm(instance=user, data=request.POST or None)

    context = {'password_change_form':form, 'userForm':userForm, 'user':request.user, 'pageheader':"Müşteri Şifre Güncelleme"}
    return render(request, 'front_end/musteri/musteri_panel.html', context)



def profile(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')



    user = request.user
    client = request.user.Client

    #form = UpdateClientForm(instance=client, data=request.POST or None)
    userForm = UpdateUserInfoForm(instance=user, data=request.POST or None)
    password_change_form = UserPasswordChangeForm(user=request.user, data=request.POST or None)


    form =""
    if request.POST:
        if userForm.is_valid():
            #form.save()
            userForm.save()
            messages.success(request, 'Güncelleme İşlemi Başarılı')
        else:
            messages.error(request, 'Güncelleme İşlemi Başarısız..!!')

    context={'user':user, 'client':client, 'password_change_form':password_change_form, 'userForm':userForm }
    return render(request, 'front_end/musteri/musteri_panel.html', context)
