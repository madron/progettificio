import re
from django.utils.translation import ugettext as _


def get_request_filename(member=None):
    request = _('request')
    if not member:
        return '{0}.pdf'.format(request)
    name = str(member).lower()
    name = re.sub('[^a-z]', '_', name)
    name = name.replace('__', '_')
    name = name.replace('__', '_')
    filename = '{0}_{1}.pdf'.format(request, name)
    return filename
