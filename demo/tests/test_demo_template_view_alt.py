from django.test import TestCase
from django.urls import reverse


class TestDemoTemnplateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('demo')
        cls.template_name = 'demo/demo-template.html'

    def test_template_view(self):
        response = self.client.get(self.url)
        # test template
        # (normally, I'd put this after status code but let's keep the same
        #   flow as before
        self.assertTemplateUsed(response, self.template_name)
        # test status code
        self.assertEqual(response.status_code, 200)
        # test location
        self.assertEqual(self.url, '/')
