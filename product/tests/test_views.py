from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product


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
