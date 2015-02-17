from django.contrib import admin
from rockman.todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
