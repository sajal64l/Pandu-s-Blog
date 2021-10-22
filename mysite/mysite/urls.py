from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'posts': PostSiteMap,
}

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}, 
        name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)