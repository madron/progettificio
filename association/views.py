from django.conf import settings
from django.views.generic import DetailView, TemplateView
from django_weasyprint.views import PDFTemplateResponseMixin
from . import models
from . import utils


class MembershipRequestModuleView(DetailView):
    model = models.ProvisionalMember
    template_name = 'association/membership_request_module.html'

    def get_context_data(self, **kwargs):
        context = super(MembershipRequestModuleView, self).get_context_data(**kwargs)
        context['PDF_INCLUDE'] = getattr(settings, 'PDF_INCLUDE', True)
        return context


class MembershipRequestModulePdfView(
        MembershipRequestModuleView, PDFTemplateResponseMixin):
    def get_filename(self):
        return utils.get_request_filename(self.object)


class EmptyMembershipRequestModuleView(TemplateView):
    template_name = 'association/membership_request_module.html'

    def get_context_data(self, **kwargs):
        context = super(EmptyMembershipRequestModuleView, self).get_context_data(**kwargs)
        context['PDF_INCLUDE'] = getattr(settings, 'PDF_INCLUDE', True)
        return context


class EmptyMembershipRequestModulePdfView(
        EmptyMembershipRequestModuleView, PDFTemplateResponseMixin):
    def get_filename(self):
        return utils.get_request_filename()
