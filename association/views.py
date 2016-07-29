from django.conf import settings
from django.views.generic import DetailView, FormView, TemplateView
from django_weasyprint.views import PDFTemplateResponseMixin
from . import forms
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


class ApproveProvisionalMembersView(FormView):
    form_class = forms.ApproveForm
    template_name = 'admin/association/provisionalmember/approve_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.selected = [int(pk) for pk in kwargs['selected'].split('-')]
        return super(ApproveProvisionalMembersView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ApproveProvisionalMembersView, self).get_context_data(**kwargs)
        context['opts'] = models.ProvisionalMember._meta
        qs = models.ProvisionalMember.objects.filter(pk__in=self.selected)
        context['verified'] = qs.filter(verified=True)
        context['unverified'] = qs.filter(verified=False)
        return context

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        return super(ApproveProvisionalMembersView, self).form_valid(form)
