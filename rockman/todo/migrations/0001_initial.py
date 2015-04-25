# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(help_text=b'A description of that needs to be done.', max_length=2000)),
                ('category', models.CharField(help_text=b'The category of the item that needs to be done.', max_length=2000)),
                ('created', models.DateTimeField(auto_now=True)),
                ('due', models.DateTimeField(help_text=b'The date this item needs to be completed.')),
                ('completed', models.DateTimeField(help_text=b'The date this item was completed and checked off.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
