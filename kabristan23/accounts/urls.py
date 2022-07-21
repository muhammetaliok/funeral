from django.contrib import admin
from django.urls import path,include
from .view import superadmin, client,musteri
from . import views
urlpatterns = [
path('user/login/', views.login_view, name = "login"),
path('user/logout/', views.logout_view, name = "logout"),
path('superadmin/add/', views.superadmin_add, name = "superadmin-add"),
path('client-register/', client.client_register, name="client-register"),
path('client-password-change/', client.client_password_change, name="client-password-change"),
]
