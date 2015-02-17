'''Models for the TODO Application'''
from django.db import models

class Todo(models.Model):
    item = models.CharField(
        max_length=2000,
        help_text='A description of that needs to be done.',
    )
    category = models.CharField(
        max_length=2000,
        help_text='The category of the item that needs to be done.',
    )
    created = models.DateTimeField(
        auto_now=True
    )
    due = models.DateField(
        help_text='The date this item needs to be completed.'
    )
    completed = models.DateField(
        blank=True,
        null=True,
        help_text='The date this item was completed and checked off.'
    )

    def clean(self):
        # Don't allow item to be blank
        if self.item is None:
            raise ValidationError('Item description is required.')