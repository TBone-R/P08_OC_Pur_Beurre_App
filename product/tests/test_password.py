from django.test import TestCase
from django.contrib.auth import get_user_model
from user.form import PasswordsChangeForm

class TesPassword(TestCase):

    def test_change(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@mail.com', password='12345678v1')

        self.assertTrue(self.user.check_password("12345678v1"))

        form_password = PasswordsChangeForm(user=self.user,data={
            "old_password": "12345678v1",
            "new_password1": "12345678v2",
            "new_password2": "12345678v2",
        })

        form_password.is_valid()

        self.assertTrue(form_password.is_valid())

        form_password.save()

        self.assertTrue(self.user.check_password("12345678v2"))

