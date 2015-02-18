from django.conf.urls import patterns, url
from rockman.todo import views

urlpatterns = patterns('',

    url(r'^assignee/(?P<assignee>\w+)/$',
        views.lookup_person,
        name='by_assignee'),
    url(r'^category/(?P<category>\w+)/$',
        views.lookup_category,
        name='by_category'),
    url(r'^save/$',
        views.save,
        name='save'),
)