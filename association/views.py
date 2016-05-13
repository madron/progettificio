import re
from django.views.generic import DetailView
from django_weasyprint.views import PDFTemplateResponseMixin
from . import models


class MembershipRequestModuleView(DetailView):
    model = models.Member
    template_name = 'association/membership_request_module.html'


class MembershipRequestModulePdfView(
        MembershipRequestModuleView, PDFTemplateResponseMixin):
    def get_filename(self):
        name = str(self.object).lower()
        name = re.sub('[^a-z]', '_', name)
        name = name.replace('__', '_')
        name = name.replace('__', '_')
        filename = 'request_{0}.pdf'.format(name)
        return filename
