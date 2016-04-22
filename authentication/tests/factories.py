import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    # password: pass
    password = 'pbkdf2_sha256$12000$GMh486z94kmq$yaxEmZjcLvlnBoKWNG2Y926givWTo739b6tqWnw8eBM='
    is_staff = True
    is_superuser = True
