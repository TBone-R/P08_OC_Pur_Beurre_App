from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import (
    HomeView,
    ProductDetailView,
    ResultListView,
    SubstituteListView,
)


class TestUrls(SimpleTestCase):

    def test_HomeView(self):
        url = reverse("product:home")
        self.assertEqual(resolve(url).func.__name__,
                         HomeView.as_view().__name__)

    def test_ProductDetailView(self):
        url = reverse("product:product", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.__name__,
                         ProductDetailView.as_view().__name__)

    def test_ResultListView(self):
        url = reverse("product:result")
        self.assertEqual(resolve(url).func.__name__,
                         ResultListView.as_view().__name__)

    def test_SubstituteListView(self):
        url = reverse("product:substitutes", kwargs={"id": 1})
        self.assertEqual(resolve(url).func.__name__,
                         SubstituteListView.as_view().__name__)
