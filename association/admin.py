from django.conf.urls import url
from django.contrib import admin
from django.utils.translation import ugettext as _
from . import forms
from . import models
from . import views


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    form = forms.MemberForm
    fieldsets = (
        (None, {'fields': (
            ('first_name', 'last_name', 'number'),
            ('place_of_birth', 'date_of_birth'),
        )}),
        (_('Residence'), {'fields': (('city', 'address', 'zip_code'),)}),
        (_('Contacts'), {'fields': (('email', 'phone_number'),)}),
        (_('Request'), {'fields': (('request_place', 'request_date'),)}),
    )
    search_fields = ('first_name', 'last_name')

    def get_urls(self):
        info = dict(app_label=self.model._meta.app_label, model_name=self.model._meta.model_name)
        request_name = '{app_label}_{model_name}_request'.format(**info)
        request_pdf_name = '{app_label}_{model_name}_request_pdf'.format(**info)
        urls = [
            url(
                r'^(?P<pk>[0-9]+)/request/$',
                self.admin_site.admin_view(views.MembershipRequestModuleView.as_view()),
                name=request_name
            ),
            url(
                r'^(?P<pk>[0-9]+)/request/pdf/$',
                self.admin_site.admin_view(views.MembershipRequestModulePdfView.as_view()),
                name=request_pdf_name
            ),
        ]
        return urls + super(MemberAdmin, self).get_urls()


class MemberProposalAdmin(MemberAdmin):
    pass


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.MemberProposal, MemberProposalAdmin)
