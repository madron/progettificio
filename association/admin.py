from django.conf.urls import url
from django.contrib import admin
from django.utils.translation import ugettext as _
from . import forms
from . import models
from . import views

# MemberAdmin fieldsets
MEMBER_MAIN_FIELDSET = (None, {'fields': [
    ('first_name', 'last_name', 'number'),
    ('place_of_birth', 'date_of_birth'),
]})
MEMBER_RESIDENCE_FIELDSET = (_('Residence'), {'fields': (('city', 'address', 'zip_code'),)})
MEMBER_RESIDENCE_FIELDSET = (_('Residence'), {'fields': (
    ('address', 'city'),
    ('province', 'zip_code'),
)})
MEMBER_CONTACTS_FIELDSET = (_('Contacts'), {'fields': (('email', 'phone_number'),)})
MEMBER_REQUEST_FIELDSET = (_('Request'), {'fields': (('request_place', 'request_date', 'approval_date'),)})
# ProvisionalMemberAdmin fieldsets
PROVISIONAL_MEMBER_MAIN_FIELDSET = (None, {'fields': [
    ('first_name', 'last_name'),
    ('place_of_birth', 'date_of_birth'),
]})
PROVISIONAL_MEMBER_RESIDENCE_FIELDSET = MEMBER_RESIDENCE_FIELDSET
PROVISIONAL_MEMBER_CONTACTS_FIELDSET = MEMBER_CONTACTS_FIELDSET
PROVISIONAL_MEMBER_REQUEST_FIELDSET = (_('Request'), {'fields': (('request_place', 'request_date', 'sign'),)})


class MemberCommonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
    form = forms.MemberForm
    readonly_fields = ('number', 'approval_date')
    search_fields = ('number', 'first_name', 'last_name', 'city', 'address', 'zip_code', 'email', 'phone_number')


class MemberAdmin(MemberCommonAdmin):
    list_display = ('number', 'first_name', 'last_name', 'email', 'phone_number', 'approval_date')
    date_hierarchy = 'approval_date'
    list_filter = ('approval_date',)
    fieldsets = (
        MEMBER_MAIN_FIELDSET,
        MEMBER_RESIDENCE_FIELDSET,
        MEMBER_CONTACTS_FIELDSET,
        MEMBER_REQUEST_FIELDSET,
    )

    def get_actions(self, request):
        actions = super(MemberAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProvisionalMemberAdmin(MemberCommonAdmin):
    list_display = ('first_name', 'last_name', 'sign')
    list_filter = ('sign',)
    exclude = ('number',)
    fieldsets = (
        PROVISIONAL_MEMBER_MAIN_FIELDSET,
        PROVISIONAL_MEMBER_RESIDENCE_FIELDSET,
        PROVISIONAL_MEMBER_CONTACTS_FIELDSET,
        PROVISIONAL_MEMBER_REQUEST_FIELDSET,
    )

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
        return urls + super(ProvisionalMemberAdmin, self).get_urls()


admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.ProvisionalMember, ProvisionalMemberAdmin)
