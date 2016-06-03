from django.views.generic import DetailView
from django_weasyprint.views import PDFTemplateResponseMixin
from . import models
from . import utils


class MembershipRequestModuleView(DetailView):
    model = models.ProvisionalMember
    template_name = 'association/membership_request_module.html'


class MembershipRequestModulePdfView(
        MembershipRequestModuleView, PDFTemplateResponseMixin):
    def get_filename(self):
        return utils.get_request_filename(self.object)
