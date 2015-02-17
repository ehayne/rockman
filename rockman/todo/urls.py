from django.conf.urls import patterns, url
from rockman.todo import views

urlpatterns = patterns('',

    url(r'^(?P<assignee>\w+)/$', views.lookup_person),
    url(r'^(?P<category>\w+)/$', views.lookup_category),
)