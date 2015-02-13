from django.conf.urls import patterns, url
from rockman.blog import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
)
