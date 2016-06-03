from django import forms
from . import models


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ('__all__')
        widgets = dict(
            province=forms.TextInput(attrs={'size': '5'}),
            zip_code=forms.TextInput(attrs={'size': '8'}),
        )
