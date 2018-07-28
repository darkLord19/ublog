from django.shortcuts import render
from django.utils import timezone
from .models import Post,Comment

def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts.html', {'posts':posts})
