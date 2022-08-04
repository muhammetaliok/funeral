from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('list/',views.list,name='list'),
path('list-details/<slug:slug>/',views.add_comment,name='add_comment'),
path('search/<str:name>/',views.search,name='search'),
path('blog/',views.blog,name='blog'),
path('blog-details/<slug:slug>/',views.blog_details,name='blog_details'),
path('add-blog/',views.add_blog,name='add_blog'),
path('update-blog/<int:id/',views.update_blog,name='update_blog'),
path('delete-blog/',views.delete_blog,name='delete_blog'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),  
path('detay-kisi/',views.detay_kisi_create,name='detay_kisi'),

path('register/', views.register_request, name='register'),
path('login/', views.login_request, name='login'),
path("logout", views.logout_request, name= "logout"),
 

################## PANEL #####################
path('user-info/',views.user_info,name='user_info'),  
path('user-post/',views.user_post,name='user_post'),  
path('user-comments/<int:id>/',views.user_comments,name='user_comments'),  
path('user-approve-comments/',views.user_approve_comments,name='user_approve_comments'),  
path('user-post/',views.user_post,name='user_post'),  
path('user-add-post/',views.user_add_post,name='user_add_post'),  
path('user-post-delete',views.user_post_delete,name='user_post_delete'),
path('user-post-edit/<int:id>',views.user_post_edit,name='user_post_edit'),  
path('user-password/',views.user_password,name='user_password'),  



path ('payment/',views.payment_method,name='payment'),

]
