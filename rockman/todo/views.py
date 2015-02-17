from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from .models import Todo

def index(request):
    template = loader.get_template('todo.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def lookup_person(request, assignee):
    """
    find the todo list for a person
    """

    list = Todo.objects.filter(assignee__iexact=assignee)

    context= {
        'name': assignee,
        'todo_list': list,
    }

    if request.user.is_authenticated():
        template = 'update_todo.html'
    else:
        template = 'view_todo.html'

    return render_to_response(template, context, RequestContext(request))


def lookup_category(request, category):
    """
    find the todo list for a category
    """

    list = Todo.objects.filter(category__iexact=category)

    context= {
        'name': category,
        'todo_list': list,
    }

    if request.user.is_authenticated():
        template = 'update_todo.html'
    else:
        template = 'view_todo.html'

    return render_to_response(template, context, RequestContext(request))