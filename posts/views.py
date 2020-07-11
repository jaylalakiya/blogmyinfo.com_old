from django.db.models import Count
from django.shortcuts import render
from .models import Post
from random import randint


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)[0:4]
    latest_five = Post.objects.order_by('-timestamp')[0:5]

    context = {
        'object_list': featured,
        'latest': latest_five,
    }
    return render(request, "index.html", context)


def blog(request):
    category_count = get_category_count()
    latest_nine = Post.objects.order_by('-timestamp')[0:9]
    featured = Post.objects.filter(featured=True)[3:7]

    context = {
        'latest': latest_nine,
        'featured': featured,
        'categories': category_count,
    }
    return render(request, "blog.html", context)


def about(request):
    return render(request, "about.html", {})


def contact(request):
    latest_two = Post.objects.order_by('-timestamp')[0:2]
    category_count = get_category_count()
    best_post = Post.objects.filter(featured=True)[randint(0, 10)]

    context = {
        'latest': latest_two,
        'categories': category_count,
        'best_post': best_post
    }
    return render(request, "contact.html", context)


def post(request, id):
    category_count = get_category_count()
    featured = Post.objects.filter(featured=True)[7:12]

    context = {
        'categories': category_count,
        'featured': featured,
    }
    return render(request, "post.html", context)
