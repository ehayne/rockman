# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20150425_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.CharField(help_text=b'Directions for preparing the recipe.', max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(help_text=b'A list of ingredients for the recipe.', max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.CharField(help_text=b'Interesting notes about the recipe.', max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
