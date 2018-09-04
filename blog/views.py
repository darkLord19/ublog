from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm, CommentForm,ContactForm
from umangparmar.privates import Const

def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts':posts})

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, slug=slug, published_date__year=year, published_date__month=month)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail', year=post.published_date.year, 
                            month=post.published_date.month, slug=post.slug)
    return render(request, 'blog/post_detail.html', {'post': post, 'form':form})

def draft_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('draft_post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', year=post.published_date.year, 
                            month=post.published_date.month, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'title': post.title})

@login_required
def draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', year=post.published_date.year, 
                            month=post.published_date.month, slug=post.slug)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home_page')

def contact_me(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            subject = name + ' contacted you from your blog'
            from_email = request.POST.get('from_email', '')
            msg = request.POST.get('msg', '')
            if name and from_email and msg:
                try:
                    send_mail(subject, msg, from_email, Const.TO_EMAIL)
                except BadHeaderError:
                    return redirect(request, 'blog/contact.html', {'bad_header': '1'})
                return redirect('contact_me')
    else:
        form=ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def about_me(request):
    return render(request, 'blog/about.html')