from datetime import date
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


def default_request_place():
    return getattr(settings, 'ASSOCIATION_DEFAULT_PLACE', '')


class MemberManager(models.Manager):
    def get_queryset(self):
        qs = super(MemberManager, self).get_queryset()
        return qs.filter(number__isnull=False)


class Member(models.Model):
    number = models.PositiveIntegerField(_('number'), null=True, unique=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=50, default='')
    last_name = models.CharField(_('last name'), max_length=50, default='')
    place_of_birth = models.CharField(_('birth place'), max_length=50, default='')
    date_of_birth = models.DateField(_('birth date'))
    # Residence
    city = models.CharField(_('city'), max_length=50, default='')
    address = models.CharField(_('address'), max_length=50, default='')
    zip_code = models.CharField(_('zip code'), max_length=10, default='')
    # Contacts
    email = models.EmailField(_('email'), blank=True)
    phone_number = models.CharField(_('phone number'), max_length=50, blank=True)
    # Request
    request_place = models.CharField(_('request place'), max_length=50, default=default_request_place)
    request_date = models.DateField(_('request date'), null=True, default=date.today)

    objects = MemberManager()

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


class MemberProposalManager(models.Manager):
    def get_queryset(self):
        qs = super(MemberProposalManager, self).get_queryset()
        return qs.filter(number__isnull=True)


class MemberProposal(Member):
    class Meta:
        proxy = True
        verbose_name = _('member proposal')
        verbose_name_plural = _('member proposals')

    objects = MemberProposalManager()
