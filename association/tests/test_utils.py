from django.test import TestCase, override_settings
from . import factories
from .. import utils


class UtilsTest(TestCase):
    def test_get_request_filename_default(self):
        member = factories.MemberFactory.build(id=1, first_name='Joe', last_name='Simon & Simon')
        filename = utils.get_request_filename(member)
        self.assertEqual(filename, 'request_joe_simon_simon.pdf')

    @override_settings(LANGUAGE_CODE='it')
    def test_get_request_filename_translated(self):
        member = factories.MemberFactory.build(id=1, first_name='Joe', last_name='Simon & Simon')
        filename = utils.get_request_filename(member)
        self.assertEqual(filename, 'domanda_joe_simon_simon.pdf')

    def test_get_request_filename_empty(self):
        filename = utils.get_request_filename()
        self.assertEqual(filename, 'request.pdf')

    @override_settings(LANGUAGE_CODE='it')
    def test_get_request_filename_empty_translated(self):
        filename = utils.get_request_filename()
        self.assertEqual(filename, 'domanda.pdf')
