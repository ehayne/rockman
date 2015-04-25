from django.conf.urls import patterns, url
from rockman.meals import views

urlpatterns = patterns('',

    url(r'^week/(?P<week_of>\w+)/$',
        views.lookup_week,
        name='by_week'),
    url(r'^',
        views.lookup_week,
        name='by_week'),
    # url(r'^category/(?P<category>\w+)/$',
    #     views.lookup_category,
    #     name='by_category'),
    # url(r'^save/$',
    #     views.save,
    #     name='save'),
)