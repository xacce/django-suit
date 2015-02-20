# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='includeblock',
            name='css_class',
            field=models.CharField(default=b'col-lg-4 col-md-4 col-sm-6', help_text=b'That field-content will be put into class="..."', max_length=255),
            preserve_default=True,
        ),
    ]
