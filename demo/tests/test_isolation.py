from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class TestIsolation(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="example")

    def test_update_first_name(self):
        # first_name is empty
        self.assertEqual(self.user.first_name, '')
        # update first_name and save to database
        self.user.first_name = "John"
        self.user.save()

        # confirm with a lookup this occurred
        u = User.objects.get(username="example")
        self.assertEqual(u.first_name, "John")

    def test_first_name_original_state(self):
        # test that first_name has returned to its original state
        self.assertEqual(self.user.first_name, "")
