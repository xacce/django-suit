from operator import attrgetter
import models as suit_models
from django.core.urlresolvers import resolve
from django.conf import settings


def include_blocks_context(request):
    if resolve(request.path).url_name == 'index':
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

        return {'include_blocks': sorted(blocks, key=attrgetter('priority'), reverse=True)}
    return {}