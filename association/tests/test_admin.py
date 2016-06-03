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


class MemberAdminTest(TestCase):
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
        self.assertEqual(response.status_code, 403)

    def test_change(self):
        obj = factories.MemberFactory()
        url = reverse('admin:association_member_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.MemberFactory()
        url = reverse('admin:association_member_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


class ProvisionalMemberAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='test')
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:association_provisionalmember_changelist')

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:association_provisionalmember_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_change(self):
        obj = factories.ProvisionalMemberFactory()
        url = reverse('admin:association_provisionalmember_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('admin:association_provisionalmember_request_pdf', args=(obj.pk,))
        self.assertContains(response, 'href="{0}"'.format(url))

    def test_delete(self):
        obj = factories.ProvisionalMemberFactory()
        url = reverse('admin:association_provisionalmember_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_request(self):
        obj = factories.ProvisionalMemberFactory()
        url = reverse('admin:association_provisionalmember_request', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_request_pdf(self):
    #     obj = factories.ProvisionalMemberFactory(id=1, first_name='Joe', last_name='Simon & Simon')
    #     url = reverse('admin:association_provisionalmember_request_pdf', args=(obj.pk,))
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['Content-Disposition'], 'attachment; filename="request_joe_simon_simon.pdf"')
