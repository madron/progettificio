from django import forms
from django.conf import settings
from django.contrib.admin.templatetags.admin_static import static
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import ugettext as _
from . import models


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ('__all__')
        widgets = dict(
            province=forms.TextInput(attrs={'size': '5'}),
            zip_code=forms.TextInput(attrs={'size': '8'}),
        )


class ApproveForm(forms.Form):
    selected = forms.models.ModelMultipleChoiceField(
        label=_('Selected'),
        queryset=models.ProvisionalMember.objects.filter(verified=True),
    )
    approval_date = forms.DateField(label=_('Approval date'), widget=AdminDateWidget)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'core.js',
            'vendor/jquery/jquery%s.js' % extra,
            'jquery.init.js',
            'admin/RelatedObjectLookups.js',
            'actions%s.js' % extra,
            'urlify.js',
            'prepopulate%s.js' % extra,
            'vendor/xregexp/xregexp.min.js',
            'calendar.js',
            'admin/DateTimeShortcuts.js',
        ]
        return forms.Media(js=[static('admin/js/%s' % url) for url in js])
