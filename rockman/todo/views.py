from django.shortcuts import render_to_response
from django.template import RequestContext

from datetime import datetime

from .models import Todo


def lookup_person(request, assignee):
    """
    find the todo list for a person
    """

    list = Todo.objects.filter(assignee__iexact=assignee)

    context= {
        'name': assignee,
        'todo_list': list,
        'type': 'assignee',
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
        'type': 'category',
    }

    if request.user.is_authenticated():
        template = 'update_todo.html'
    else:
        template = 'view_todo.html'

    return render_to_response(template, context, RequestContext(request))

def save(request):
    """
    validate list and save it
    """

    name = request.POST.get('name','')
    type = request.POST.get('type','')

    list=request.POST.getlist('id')
    print(list)

    if list is None:
        return request.path

    for id in list:
        #unchecked boxes are not submitted in a POST
        try:
            task = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            print('not found')  # TODO: how to handle this??
        task.completed = datetime.now()
        task.full_clean()
        task.save()

    kwargs = {type+'__iexact': name}
    todo_list = Todo.objects.filter(**kwargs)

    context = {
        'name': name,
        'todo_list': todo_list,
        'type': type,
    }

    template = 'update_todo.html'

    return render_to_response(template, context, RequestContext(request))