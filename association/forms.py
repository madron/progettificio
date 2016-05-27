from django import forms
from . import models


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ('__all__')
        widgets = dict(
            zip_code=forms.TextInput(attrs={'size': '8'}),
        )
