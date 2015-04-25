# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('meal_type', models.CharField(help_text=b'A label to be used for meals (ex. breakfast).', max_length=100)),
                ('priority', models.IntegerField(help_text=b'Order that the meal types fall in a day.', unique=True)),
                ('description', models.CharField(help_text=b'A description of the meal type.', max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(help_text=b'A description of what needs to be done.', max_length=200)),
                ('ingredients', models.CharField(help_text=b'A list of ingredients for the recipe.', max_length=2000)),
                ('directions', models.CharField(help_text=b'Directions for preparing the recipe.', max_length=2000)),
                ('notes', models.CharField(help_text=b'Interesting notes about the recipe.', max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_type',
            field=models.ForeignKey(db_column=b'meal_type', blank=True, to='meals.MealType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meal',
            name='recipes',
            field=models.ForeignKey(db_column=b'recipies', blank=True, to='meals.Recipe', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day',
            name='meals',
            field=models.ForeignKey(db_column=b'meals', blank=True, to='meals.Meal', null=True),
            preserve_default=True,
        ),
    ]
