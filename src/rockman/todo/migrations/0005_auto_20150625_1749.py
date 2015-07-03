# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20150217_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignee',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'assignee',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AlterField(
            model_name='todo',
            name='assignee',
            field=models.ForeignKey(db_column=b'assignee', blank=True, to='todo.Assignee', null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(db_column=b'category', blank=True, to='todo.Category', null=True),
        ),
        migrations.AlterModelTable(
            name='todo',
            table='todo',
        ),
    ]
