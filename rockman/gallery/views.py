from django.http import HttpResponse
from django.template import RequestContext, loader

from photologue.models import Gallery

def index(request):
    template = loader.get_template('under_construction.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def gallery(request):

    wedding_photos = Gallery.objects.filter(tags='wedding')

    template = loader.get_template('gallery.html')
    context = RequestContext(request, {
        'object_list': wedding_photos,
    })
    return HttpResponse(template.render(context))