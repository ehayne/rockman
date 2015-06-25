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
    category = models.ForeignKey(
        'Category',
        db_column='category',
        blank=True,
        null=True,
    )
    assignee = models.ForeignKey(
        'Assignee',
        db_column='assignee',
        blank=True,
        null=True,
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

    class Meta:
        db_table = 'todo'

    def __unicode__(self):
        return self.task

    def clean(self):
        # Don't allow task to be blank
        if self.task is None:
            raise ValidationError('Task description is required.')


class Assignee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'assignee'

    def __unicode__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'category'

    def __unicode__(self):
        return self.name