from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('contact', views.contact_me, name='contact_me'),
    path('about', views.about_me, name='about_me'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/publish/<int:pk>', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]