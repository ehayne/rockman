from django.shortcuts import render_to_response
from django.template import RequestContext

from rockman.todo.models import Category, Assignee, Todo

from datetime import datetime

from .models import Todo


def todo_list(request):
    """
    search for todo's by category and/or assignee
    """

    categories = Category.objects.values('name')
    assignees = Assignee.objects.values('name')

    context= {
        'category_list': categories,
        'assignee_list': assignees,
    }

    template = 'search_form.html'

    return render_to_response(template, context, RequestContext(request))


def lookup_person(request, assignee):
    """
    find the todo list for a person
    """

    assignee_id = Assignee.objects.filter(name__iexact=assignee)
    list = Todo.objects.filter(assignee=assignee_id)

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

    category_id = Category.objects.filter(name__iexact=category)
    list = Todo.objects.filter(category__iexact=category_id)

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