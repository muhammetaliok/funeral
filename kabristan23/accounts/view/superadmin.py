from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from ..forms import UserRegisterForm, ClientRegisterForm, SuperadminRegisterForm, LoginForm, UserUpdateForm,UserPasswordChangeForm, DutyForm
from ..models import Client, Superadmin, Duty
from ..views import get_auth


def superadmin_register(request):

    if request.POST:
        form = UserRegisterForm(request.POST)
        superadmin_form = SuperadminRegisterForm(request.POST)
        if form.is_valid() and superadmin_form.is_valid():
            user = form.save()
            superadmin = superadmin_form.save(commit=False)
            superadmin.user = user
            superadmin.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Giriş İşlemi Başarılı')
            return redirect('website:eytpanelv1')
        else:
            messages.error(request, 'Süper admin oluşturma işlemi başarısız')
    else:
        form = UserRegisterForm()
        superadmin_form = SuperadminRegisterForm()
    context = {'form': form, 'superadmin_form': superadmin_form}
    return render(request, 'accounts/superadmin/register/register.html', context)


def client_update(request, slug):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)

    superadmin = get_object_or_404(Superadmin, user=request.user)
    client = get_object_or_404(Client, slug=slug)

    form = UserUpdateForm(instance=client.user, data=request.POST or None)
    client_form = ClientRegisterForm(instance=client, data=request.POST or None)

    if request.POST:
        if client_form.is_valid() and form.is_valid():
            form.save()
            client_form.save()
            messages.success(request, 'Güncelleme İşlemi Başarılı')
            return redirect('adminpanel:client-list')
        else:
            messages.error(request, 'Güncelleme İşlemi Başarısız')

    context = {'form': form, 'client_form': client_form, 'pageheader':"Müşteri Güncelleme"}
    return render(request, 'accounts/client/client_update.html', context)


def superadmin_update(request):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)

    superadmin = get_object_or_404(Superadmin, user=request.user)
    form = UserUpdateForm(instance=superadmin.user, data=request.POST or None)
    superadmin_form = SuperadminRegisterForm(instance=superadmin, data=request.POST or None)

    if request.POST:
        if form.is_valid() and superadmin_form.is_valid():
            form.save()
            superadmin_form.save()
            messages.success(request, 'Güncelleme İşlemi Başarılı')
            return redirect('accounts:superadmin-update')
        else:
            messages.error(request, 'Güncelleme İşlemi Başarısız')
    company_info, company_image = get_company()
    context = {'form': form, 'superadmin_form': superadmin_form, 'pageheader':'Admin Güncelle','company_info':company_info, 'company_image':company_image}
    return render(request, 'accounts/superadmin/superadmin_update.html', context)


def client_password_change_from_admin(request, slug):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)
    client = get_object_or_404(Client, slug=slug)
    form = UserPasswordChangeForm(user=client.user, data=request.POST or None)
    if request.POST:
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            client.user.set_password(new_password)
            client.user.save()
            update_session_auth_hash(request, client.user)
            messages.success(request, 'Güncelleme İşlemi Başarılı')
            return redirect('adminpanel:client-list')
        else:
            messages.error(request, 'Güncelleme İşlemi Başarısız.!!')
    context = {'form':form, 'slug':client.slug ,'pageheader':"Müşteri Şifresini Güncelleme"}
    return render(request, 'accounts/client/client_password_change_from_admin.html', context)


def superadmin_password_change(request):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)
    form = UserPasswordChangeForm(user=request.user, data=request.POST or None)
    if request.POST:
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Güncelleme İşlemi Başarılı')
            return redirect('accounts:superadmin-password-change')
        else:
            messages.error(request, 'Güncelleme İşlemi Başarısız')
    company_info, company_image = get_company()
    context = {'form':form, 'pageheader':'Admin Şifre Değiştirme','company_info':company_info, 'company_image':company_image}
    return render(request, 'accounts/superadmin/superadmin_password_change.html', context)


def client_delete(request, slug):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)
    client = get_object_or_404(Client, slug=slug)
    user = client.user
    client.delete()
    user.delete()
    messages.success(request, 'Silme İşlemi Başarılı')
    return redirect('adminpanel:client-list')


def add_list_duty(request):
    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)

    superadmin = get_object_or_404(Superadmin, user=request.user)
    dutys = Duty.objects.all()
    if request.POST:
        form = DutyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kullanıcı Görevi Ekleme İşlemi Başarılı')
            return redirect('accounts:add-list-duty')
        else:
            messages.error(request, 'Kullanıcı Görevi Ekleme İşlemi Başarısız')
    else:
        form = DutyForm()
    context = {'form': form, 'dutys':dutys ,'pageheader': 'Kullanıcı Bilgilerini Güncelle'}
    return render(request, 'accounts/superadmin/add_list_duty.html', context)


def add_client(request):

    flag, gidilecek_sayfa = get_auth(request)
    if flag:
        return redirect(gidilecek_sayfa)

    superadmin = get_object_or_404(Superadmin, user=request.user)

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
            messages.success(request, 'Müşteri Ekleme İşlemi Başarılı')
            return redirect('adminpanel:client-list')
        else:
            messages.error(request, 'Müşteri Ekleme İşlemi Başarısız')
    else:
        form = UserRegisterForm()
        client_form = ClientRegisterForm()
    company_info, company_image = get_company()
    context = {'form': form, 'client_form': client_form, 'pageheader': 'Müşteri Ekleme','company_info':company_info, 'company_image':company_image}
    return render(request, 'accounts/superadmin/add_client.html', context)
