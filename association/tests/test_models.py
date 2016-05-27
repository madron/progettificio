from django.test import TestCase
from . import factories


class MemberModelTest(TestCase):
    def test_str(self):
        member = factories.MemberFactory.build(first_name='Joe', last_name='Black')
        self.assertEqual(str(member), 'Joe Black')
