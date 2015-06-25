# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateField(help_text=b'The date this item was completed and checked off.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateField(help_text=b'The date this item needs to be completed.'),
            preserve_default=True,
        ),
    ]
