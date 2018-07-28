from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comment

def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts.html', {'posts':posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})