from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('contact', views.contact_me, name='contact_me'),
    path('about', views.about_me, name='about_me'),
    path('posts/<slug:slug>', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('posts/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('posts/<int:pk>/remove/', views.post_remove, name='post_remove'),
]