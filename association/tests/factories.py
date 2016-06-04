import factory
from factory.django import DjangoModelFactory
from .. import models


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = models.Member

    number = factory.Sequence(lambda n: n)
    first_name = 'Joe'
    last_name = 'Black'
    date_of_birth = '1990-01-01'
    request_place = 'London'
    request_date = '2016-01-01'
    approval_date = '2016-01-30'
    verified = True


class ProvisionalMemberFactory(MemberFactory):
    class Meta:
        model = models.ProvisionalMember

    number = None
    approval_date = None
    verified = False
