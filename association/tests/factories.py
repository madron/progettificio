from factory.django import DjangoModelFactory
from .. import models


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = models.Member

    name = 'Joe'
    surname = 'Black'
