from django.test import TestCase
from .. import forms


class MemberFormTest(TestCase):
    def test_clean(self):
        data = dict(
            first_name='Joe',
            last_name='Black',
            place_of_birth='London',
            date_of_birth='1990-01-01',
            city='London',
            address='Narrow street',
            zip_code='12345',
            request_place='London',
            request_date='2015-01-01',
        )
        form = forms.MemberForm(data)
        self.assertEqual(form.errors, {})
