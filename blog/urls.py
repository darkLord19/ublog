from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemap import SITEMAPS
from .feed import LatestEntriesFeed

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact', views.contact_me, name='contact_me'),
    path('about', views.about_me, name='about_me'),
    path('archives', views.archives_view, name='archive'),
    path('<int:year>/<int:month>/<slug:slug>', views.post_detail, name='post_detail'),
    path('archive/<int:year>', views.year_archive, name='year_archive'),
    path('archive/<int:year>/<int:month>', views.month_archive, name='month_archive'),
    path('category/<category>', views.posts_by_category, name='posts_by_category'),
    path('new', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('drafts/<int:pk>', views.draft_post_detail, name='draft_post_detail'),
    path('<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed', LatestEntriesFeed()),
]
