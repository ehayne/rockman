from django.conf import settings
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from rockman.settings import SOCIAL_AUTH_LOGIN_URL


urlpatterns = patterns(
    '',
    url(r'^ping$', lambda x: HttpResponse('pong')),
    url(r'^', include('rockman.base.urls')),
    # These go togeather to override admin login to use social auth
    url(r'^admin/login/', RedirectView.as_view(url='/social/login/github-org')),
    url(r'^accounts/profile/', RedirectView.as_view(url='/admin')),
    #
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)blog/', include('rockman.blog.urls')),
    url(r'^(?i)gallery/', include('rockman.gallery.urls')),
    url(r'^(?i)todo/', include('rockman.todo.urls')),
    url(r'^(?i)meals/', include('rockman.meals.urls')),
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?i)photologue/', include('photologue.urls', namespace="photologue")),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
urlpatterns += staticfiles_urlpatterns()