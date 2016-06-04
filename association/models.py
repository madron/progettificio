from datetime import date
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


def default_request_place():
    return getattr(settings, 'ASSOCIATION_DEFAULT_PLACE', '')


class MemberManager(models.Manager):
    def get_queryset(self):
        qs = super(MemberManager, self).get_queryset()
        return qs.filter(approval_date__isnull=False)


class Member(models.Model):
    number = models.PositiveIntegerField(_('number'), null=True, unique=True, blank=True, db_index=True)
    first_name = models.CharField(_('first name'), max_length=50, default='', db_index=True)
    last_name = models.CharField(_('last name'), max_length=50, default='', db_index=True)
    place_of_birth = models.CharField(_('birth place'), max_length=50, default='')
    date_of_birth = models.DateField(_('birth date'))
    # Residence
    address = models.CharField(_('address'), max_length=50, default='', db_index=True)
    city = models.CharField(_('city'), max_length=50, default='', db_index=True)
    province = models.CharField(_('province'), max_length=50, default='', db_index=True)
    zip_code = models.CharField(_('zip code'), max_length=10, default='')
    # Contacts
    email = models.EmailField(_('email'), blank=True, db_index=True)
    phone_number = models.CharField(_('phone number'), max_length=50, blank=True, db_index=True)
    # Request
    request_place = models.CharField(_('request place'), max_length=50, default=default_request_place)
    request_date = models.DateField(_('request date'), null=True, default=date.today)
    verified = models.BooleanField(_('verified'), default=False, db_index=True)
    approval_date = models.DateField(_('approval date'), null=True, blank=True, db_index=True)

    objects = MemberManager()

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)


class ProvisionalMemberManager(models.Manager):
    def get_queryset(self):
        qs = super(ProvisionalMemberManager, self).get_queryset()
        return qs.filter(approval_date__isnull=True)


class ProvisionalMember(Member):
    class Meta:
        proxy = True
        verbose_name = _('provisional member')
        verbose_name_plural = _('provisional members')

    objects = ProvisionalMemberManager()
