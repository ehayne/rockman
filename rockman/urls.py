from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^', include('rockman.base.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)blog/', include('rockman.blog.urls')),
    url(r'^(?i)gallery/', include('rockman.gallery.urls')),
    url(r'^(?i)todo/', include('rockman.todo.urls')),
)
