from factory.django import DjangoModelFactory
from .. import models


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = models.Member

    first_name = 'Joe'
    last_name = 'Black'
    date_of_birth = '1990-01-01'
