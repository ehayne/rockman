from django.shortcuts import render_to_response
from django.template import RequestContext

from datetime import datetime

# from .models import Meals


def lookup_week(request, week_of='default place holder'):
    """
    find the meals for 7 days starting with week_of date
    """

    # list = Todo.objects.filter(assignee__iexact=assignee)
    #
    meal_list =['1','2','3']

    context= {
        'week_of': week_of,
        'meal_list': meal_list,
    }
    template='week.html'
    #
    # if request.user.is_authenticated():
    #     template = 'update_todo.html'
    # else:
    #     template = 'view_todo.html'

    return render_to_response(template, context, RequestContext(request))