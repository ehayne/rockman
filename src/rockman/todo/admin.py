from django.contrib import admin
from rockman.todo.models import Todo, Assignee,Category

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'category', 'assignee',)
admin.site.register(Todo, TodoAdmin)


class AssigneeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignee, AssigneeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)