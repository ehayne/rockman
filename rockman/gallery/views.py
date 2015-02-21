from django.http import HttpResponse
from django.template import RequestContext, loader

from photologue.models import Gallery


def index(request):
    template = loader.get_template('under_construction.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def gallery(request):

    photos = Gallery.objects.all()

    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'object_list': photos,
        'extra_js_file': ['gallery/fancybox/lib/jquery.mousewheel-3.0.6.pack.js',
                          'gallery/fancybox/source/jquery.fancybox.pack.js',
                          'gallery/fancybox/source/helpers/jquery.fancybox-buttons.js',
                          'gallery/fancybox/source/helpers/jquery.fancybox-media.js',
                          'gallery/fancybox/source/helpers/jquery.fancybox-thumbs.js'],
        'extra_css_file': ['gallery/fancybox/source/jquery.fancybox.css',
                           'gallery/fancybox/source/helpers/jquery.fancybox-buttons.css',
                           'gallery/fancybox/source/helpers/jquery.fancybox-thumbs.css'],
    })
    return HttpResponse(template.render(context))