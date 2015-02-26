from __future__ import print_function
import sys


def include_blocks_context(request):
    print('Deprecated: do not use suit context processor. '
          'Dell <suit.context.include_blocks_context> from yout TEMPLATE_CONTEXT_PROCESSORS', file=sys.stderr)
    return {}