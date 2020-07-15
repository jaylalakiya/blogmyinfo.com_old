from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import index, blog, about, contact, post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<title>/', post, name='post-detail'),
    path('about/', about),
    path('contact/', contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
