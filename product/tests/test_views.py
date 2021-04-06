from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def test_substitute_list(self):

        client = Client()

        response = client.get(reverse("product:product", kwargs={"id": 1}))

        self.assertEqual(response.status_code, 404)

        product = Product.objects.create(
            name="test 1",
            brand="",
            nova=0,
            nutri_score="",
            image_url=""
        )

        response = client.get(reverse("product:product",
                                      kwargs={"id": product.id}))

        self.assertEqual(response.status_code, 200)

    def test_home(self):
        client = Client()

        response = client.get(reverse("product:home"))

        self.assertEqual(response.status_code, 200)

    def test_detail(self):

        client = Client()

        response = client.get(reverse("product:product", kwargs={"id": 1}))

        self.assertEqual(response.status_code, 404)

        product = Product.objects.create(
            name="test 1",
            brand="",
            nova=0,
            nutri_score="",
            image_url=""
        )

        response = client.get(reverse("product:product",
                                      kwargs={"id": product.id}))

        self.assertEqual(response.status_code, 200)

    def test_result_list(self):

        client = Client()

        response = client.get(reverse("product:product", kwargs={"id": 1}))

        self.assertEqual(response.status_code, 404)

        product = Product.objects.create(
            name="test 1",
            brand="",
            nova=0,
            nutri_score="",
            image_url=""
        )

        response = client.get(reverse("product:product",
                                      kwargs={"id": product.id}))

        self.assertEqual(response.status_code, 200)

    def test_password_change(self):

        client = Client()

        self.user = get_user_model().objects.create_user(
            email='testuser@mail.com', password='12345',
            order_by_1='nova',
            order_by_2='nova',
            order_by_3='nova',
            order_by_4='nova')
        self.client.login(email='testuser@mail.com', password='12345')

        response = client.get(reverse("account:password_change"))

        self.assertEqual(response.status_code, 302)

        response = client.get(reverse("account:password_change"), follow=True)

        self.assertEqual(response.status_code, 200)

