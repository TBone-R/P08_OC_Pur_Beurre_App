from django.test import TestCase
from product.queryset import get_order
from constant import ORDER_BY
from django.contrib.auth import get_user_model


class TestSubstitute(TestCase):

    def test_order_1(self):

        self.user = get_user_model().objects.create_user(
            email='testuser@mail.com', password='12345')
        self.client.login(email='testuser@mail.com', password='12345')

        list_assert = get_order(self.user)

        result = [i[1] for i in ORDER_BY]

        self.assertEqual(list_assert, result)

    def test_order_2(self):

        self.user = get_user_model().objects.create_user(
            email='testuser@mail.com', password='12345',
            order_by_1='nova',
            order_by_2='nova',
            order_by_3='nova',
            order_by_4='nova')
        self.client.login(email='testuser@mail.com', password='12345')

        list_assert = get_order(self.user)

        result = ['nova', 'nova', 'nova', 'nova']

        self.assertEqual(list_assert, result)
