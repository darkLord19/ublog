from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact_me, name='contact_me'),
    path('about', views.about_me, name='about_me'),
    path('<int:year>/<int:month>/<slug:slug>', views.post_detail, name='post_detail'),
    path('new', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('drafts/<int:pk>', views.draft_post_detail, name='draft_post_detail'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/remove/', views.post_remove, name='post_remove'),
]
