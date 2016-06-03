import re
from django.utils.translation import ugettext as _


def get_request_filename(member):
    name = str(member).lower()
    name = re.sub('[^a-z]', '_', name)
    name = name.replace('__', '_')
    name = name.replace('__', '_')
    request = _('request')
    filename = '{0}_{1}.pdf'.format(request, name)
    return filename
