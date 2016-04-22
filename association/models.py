from django.db import models
from django.utils.translation import ugettext as _


class Member(models.Model):
    surname = models.CharField(_('surname'), max_length=200)
    name = models.CharField(_('name'), max_length=200)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('surname', 'name')

    def __str__(self):
        return '{name} {surname}'.format(surname=self.surname, name=self.name)
