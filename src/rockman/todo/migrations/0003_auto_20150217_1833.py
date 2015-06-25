# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20150217_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='item',
        ),
        migrations.AddField(
            model_name='todo',
            name='assignee',
            field=models.CharField(help_text=b'The person assigned to this task.', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='task',
            field=models.CharField(default='text', help_text=b'A description of what needs to be done.', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.CharField(help_text=b'The category of the task that needs to be done.', max_length=2000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateField(help_text=b'The date this task was completed and checked off.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateField(help_text=b'The date this task needs to be completed.'),
            preserve_default=True,
        ),
    ]
