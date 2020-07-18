from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=50, default='max_length is 50 characters')
    meta_description = models.CharField(
        max_length=200, default='max_length is 200 characters')
    meta_keywords = models.TextField(
        default='Enter the keywords like: word1, word2, word3,...')
    overview = models.CharField(
        max_length=120, default='max_length is 120 characters')
    content = RichTextUploadingField(default='Enter your content here')
    timestamp = models.DateTimeField(auto_now_add=True)
    # view_count = models.IntegerField(default=0)
    # comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, default='beast', on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'title': self.title
        })

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


class News(models.Model):
    title = models.CharField(max_length=150, default="title")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
