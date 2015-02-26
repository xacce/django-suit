from operator import attrgetter
from django import template
from suit import models as suit_models
from django.conf import settings

register = template.Library()

@register.assignment_tag
def get_include_blocks():
    blocks = list(suit_models.IncludeBlock.objects.all())
    try:
        for item in settings.SUIT_INCLUDE_BLOCKS:
            template = item.get('template_path', None)
            css_class = item.get('css_class', 'col-lg-4 col-md-4 col-sm-6')
            priority = int(item.get('priority', 0))
            if template:
                new_block = suit_models.IncludeBlock(template_path=template, css_class=css_class, priority=priority)
                blocks.append(new_block)
    except (AttributeError, ValueError):
        pass

    return sorted(blocks, key=attrgetter('priority'), reverse=True)