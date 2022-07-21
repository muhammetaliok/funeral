from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from ..forms import UserRegisterForm, ClientRegisterForm, UserPasswordChangeForm
from ..models import Client
from ..decorators import unauthenticated_user


def client_register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        client_form = ClientRegisterForm(request.POST)
        if form.is_valid() and client_form.is_valid():
            user = form.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('website:home')
    else:
        form = UserRegisterForm()
        client_form = ClientRegisterForm()

    context = {'form': form, 'client_form': client_form}
    return render(request, 'front_end/accounts/client/register/register.html', context)

def client_password_change(request):
    form = UserPasswordChangeForm(user=request.user, data=request.POST or None)
    if request.POST:
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Şifre Güncelleme İşlemi Başarılı')
            return redirect('website:index')
        else:
            messages.error(request, 'Şifre Güncelleme İşlemi Başarısız.!!')
    context = {'form':form, 'pageheader':"Müşteri Şifre Güncelleme"}
    return render(request, 'website/index/client_password_change.html', context)
