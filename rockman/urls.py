from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns('',

    url(r'^', include('rockman.base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)blog/', include('rockman.blog.urls')),
    url(r'^(?i)gallery/', include('rockman.gallery.urls')),
    url(r'^(?i)todo/', include('rockman.todo.urls')),
    url(r'^(?i)meals/', include('rockman.meals.urls')),

    url(r'^(?i)photologue/', include('photologue.urls', namespace="photologue")),
)

if settings.APP_ENV == 'local':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)