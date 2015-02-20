import models as suit_models
from django.core.urlresolvers import resolve


def include_blocks_context(request):
    if resolve(request.path).url_name == 'index':
        return {'include_blocks': suit_models.IncludeBlock.objects.all().order_by('-priority')}
    return {}