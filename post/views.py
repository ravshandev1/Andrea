from django.shortcuts import render
from .models import *
from contact.models import Subscribe
from .forms import CommentForm


# Create your views here.

def home(request):
    posts = Post.objects.order_by('-id')
    s = request.GET.get('s')
    if s:
        posts = posts.filter(title__icontains=s)
    t = request.GET.get('t')
    if t:
        posts = posts.filter(tags__tag__exact=t)
    c = request.GET.get('c')
    if c:
        posts = posts.filter(category__category__exact=c)
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    ctx = {
        'posts': posts
    }
    return render(request, 'index.html', ctx)


def blog_single(request, pk):
    post = Post.objects.get(id=pk)
    post.views += 1
    post.save()
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        commit = form.save(commit=False)
        commit.post = post
        commit.save()

    ctx = {
        'post': post,
        'form': form,
    }
    return render(request, 'single.html', ctx)


def fashion(request):
    posts = Post.objects.filter(type=0)
    ctx = {
        'posts': posts
    }
    return render(request, 'fashion.html', ctx)


def travel(request):
    posts = Post.objects.filter(type=1)
    q = request.GET.get('q')
    if q:
        posts = Post.objects.filter(author_name=q)
    ctx = {
        'posts': posts
    }
    return render(request, 'travel.html', ctx)
