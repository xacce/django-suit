# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suit', '0002_includeblock_css_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='includeblock',
            name='priority',
            field=models.IntegerField(default=0, help_text=b'The bigger, the better'),
            preserve_default=True,
        ),
    ]
