from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Post, News
from random import randint


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)[0:4]
    latest_five = Post.objects.order_by('-timestamp')[0:5]
    category_count = get_category_count()
    news_list = News.objects.order_by('-timestamp')[0:3]

    context = {
        'object_list': featured,
        'latest': latest_five,
        'categories': category_count,
        'news_list': news_list
    }
    return render(request, "index.html", context)


def blog(request):
    category_count = get_category_count()
    latest_nine = Post.objects.order_by('-timestamp')[0:9]
    featured = Post.objects.filter(featured=True)[3:7]
    news_list = News.objects.order_by('-timestamp')[0:3]

    context = {
        'latest': latest_nine,
        'featured': featured,
        'categories': category_count,
        'news_list': news_list
    }
    return render(request, "blog.html", context)


def about(request):
    news_list = News.objects.order_by('-timestamp')[0:3]
    latest_three = Post.objects.order_by('-timestamp')[0:3]

    featured_two = Post.objects.filter(featured=True)[0:2]

    contex = {
        'news_list': news_list,
        'latest_posts': latest_three,
        'featured_posts': featured_two,
    }
    return render(request, "about.html", contex)


def contact(request):
    latest_three = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()
    best_post = Post.objects.filter(featured=True)[randint(0, 10)]
    news_list = News.objects.order_by('-timestamp')[0:3]

    context = {
        'latest': latest_three,
        'categories': category_count,
        'best_post': best_post,
        'news_list': news_list
    }
    return render(request, "contact.html", context)


def post(request, title):
    category_count = get_category_count()
    featured = Post.objects.filter(featured=True)[7:12]
    post = get_object_or_404(Post, title=title)
    news_list = News.objects.order_by('-timestamp')[0:3]

    context = {
        'categories': category_count,
        'featured': featured,
        'post': post,
        'news_list': news_list
    }
    return render(request, "post.html", context)
