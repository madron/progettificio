from django.test import TestCase
from . import factories


class MemberModelTest(TestCase):
    def test_str(self):
        member = factories.MemberFactory.build(name='Joe', surname='Black')
        self.assertEqual(str(member), 'Joe Black')
