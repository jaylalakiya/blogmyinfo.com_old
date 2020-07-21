from django.contrib import admin

from .models import Author, Category, Post, News


# registering 'Author' model
admin.site.register(Author)


# registering 'Category' model
admin.site.register(Category)


# registering 'Post' model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', 'author', 'featured')
    list_filter = ('categories', 'featured', 'timestamp', 'author')
    raw_id_fields = ('author')
    ordering = ('timestamp')


# registering 'News' model
admin.site.register(News)
