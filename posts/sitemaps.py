from django.contrib.sitemaps import Sitemap
from .models import Post, News


class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all()
