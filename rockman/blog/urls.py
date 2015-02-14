from django.conf.urls import patterns, url, include
from rockman.blog import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
)
