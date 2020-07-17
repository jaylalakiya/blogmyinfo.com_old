from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from .models import Post, News
from contacts.models import ContactUser


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)[0:4]
    latest_five = Post.objects.order_by('-timestamp')[0:5]
    category_count = get_category_count()
    news_list = News.objects.order_by('-timestamp')[0:3]
    best_post = Post.objects.all()[0]

    context = {
        'object_list': featured,
        'latest': latest_five,
        'categories': category_count,
        'news_list': news_list
        'best_post': best_post
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
    # TODO fix the selection of best post on some basis rather than selecting from featured
    best_post = Post.objects.filter(featured=True)[0:1]
    news_list = News.objects.order_by('-timestamp')[0:3]

    context = {
        'latest': latest_three,
        'categories': category_count,
        'best_post': best_post,
        'news_list': news_list

    }

    # for actual form data
    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_subject = request.POST['contact_subject']
        contact_message = request.POST['contact_message']

        new_contact = ContactUser()
        new_contact.name = contact_name
        new_contact.email = contact_email
        new_contact.subject = contact_subject
        new_contact.message = contact_message
        new_contact.save()

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
