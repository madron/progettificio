from django.core.urlresolvers import reverse
from django.test import TestCase
from authentication.tests.factories import UserFactory
from . import factories


class AppAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='test')
        self.assertTrue(self.client.login(username='test', password='pass'))

    def test_app_index(self):
        url = reverse('admin:app_list', args=('association',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class UserAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='test')
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:association_member_changelist')

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:association_member_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        obj = factories.MemberFactory()
        url = reverse('admin:association_member_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.MemberFactory()
        url = reverse('admin:association_member_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_request(self):
        obj = factories.MemberFactory()
        url = reverse('admin:association_member_request', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
