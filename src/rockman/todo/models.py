'''Models for the TODO Application'''
from django.db import models

class Todo(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    task = models.CharField(
        max_length=2000,
        help_text='A description of what needs to be done.',
    )
    category = models.CharField(
        max_length=2000,
        help_text='The category of the task that needs to be done.',
        blank=True,
    )
    assignee = models.CharField(
        max_length=200,
        help_text='The person assigned to this task.',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now=True
    )
    due = models.DateField(
        help_text='The date this task needs to be completed.'
    )
    completed = models.DateField(
        blank=True,
        null=True,
        help_text='The date this task was completed and checked off.'
    )

    def clean(self):
        # Don't allow task to be blank
        if self.task is None:
            raise ValidationError('Task description is required.')