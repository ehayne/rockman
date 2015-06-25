# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealtype',
            name='description',
            field=models.CharField(help_text=b'A description of the meal type.', max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
