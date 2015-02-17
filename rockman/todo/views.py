from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from .models import Todo

def index(request):
    template = loader.get_template('todo.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def lookup_person(request):
    """
    find the todo list for a person
    """

    item = 'test'

    todo = Todo.objects.get(item__iexact=item.strip())

    context= {
        'list': todo
    }

    template = 'todo.html'

    return render_to_response(template, context, RequestContext(request))