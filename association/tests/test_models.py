from django.test import TestCase, override_settings
from . import factories
from .. import models


class MemberModelTest(TestCase):
    def setUp(self):
        self.data = dict(
            first_name='Joe',
            last_name='Black',
            place_of_birth='London',
            date_of_birth='1990-01-01',
            city='London',
            address='Narrow street',
            zip_code='12345',
        )

    def test_str(self):
        member = factories.MemberFactory.build(first_name='Joe', last_name='Black')
        self.assertEqual(str(member), 'Joe Black')

    @override_settings(ASSOCIATION_DEFAULT_PLACE='Headquarter')
    def test_default_request_place(self):
        member = models.Member.objects.create(**self.data)
        self.assertEqual(member.request_place, 'Headquarter')
