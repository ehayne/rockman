from django.conf.urls import patterns, url
from rockman.base import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
)