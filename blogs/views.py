from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm, RegistrationForm

def home(request):
    blog_posts = BlogPost.objects.all().order_by('-date_added')
    return render(request, 'blogs/home.html', {'blog_posts': blog_posts})

def blog_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blogs/blog.html', {'blog_posts': blog_posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blogs:blog')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if post.author != request.user:
        return HttpResponse("У вас нет прав для редактирования этой записи.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})

@login_required
def blog_view(request):
    user = request.user
    user_posts = BlogPost.objects.filter(author=user).order_by('-date_added')
    other_posts = BlogPost.objects.exclude(author=user).order_by('-date_added')

    context = {
        'user_posts': user_posts,
        'other_posts': other_posts,
    }

    return render(request, 'blogs/blog.html', context)
