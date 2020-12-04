from django.test import TestCase
from product.management.commands.sample import Command
from product.models import Category, Product
from mock import patch


class TestSample(TestCase):

    def test_get_keys(self):
        test = [
            {
                "unused_key": "unused_val",
                "product_name": "product_name",
            }, {
                "generic_name": "generic_name",
                "brands_tags": "brands_tags",
                "categories_tags": "categories_tags",
                "origins_tags": "origins_tags",
                "stores": "stores",
                "labels_tags": "labels_tags",
                "nova_group": "nova_group",
                "nutrition_grade_fr": "nutrition_grade_fr",
                "nutrient_levels": None,
                "image_url": "image_url",
                "url": "url",

            }, {
                "unused_key1": "unused_val",
                "unused_key2": "unused_val",
                "unused_key3": "unused_val",
            }]

        result = [
            {
                "product_name": "product_name",
                "generic_name": None,
                "brands_tags": None,
                "categories_tags": None,
                "labels_tags": None,
                "nova_group": None,
                "nutrition_grade_fr": None,
                "nutrient_levels": None,
                "url": None,
                "image_url": None
            }, {
                "product_name": None,
                "generic_name": "generic_name",
                "brands_tags": "brands_tags",
                "categories_tags": "categories_tags",
                "labels_tags": "labels_tags",
                "nova_group": "nova_group",
                "nutrition_grade_fr": "nutrition_grade_fr",
                "url": "url",
                "nutrient_levels": None,
                "image_url": "image_url"
            }, {
                "product_name": None,
                "generic_name": None,
                "brands_tags": None,
                "categories_tags": None,
                "labels_tags": None,
                "nova_group": None,
                "nutrition_grade_fr": None,
                "url": None,
                "image_url": None,
                "nutrient_levels": None,
            }]

        self.assertEqual(Command.get_keys(test), result)

    def test_save(self):
        self.assertEqual(Command.save_many_to_many(None, None), None)

        list_name = ['category_test1', 'category_test2']

        list_assert = Command.save_many_to_many(list_name, Category)

        result = [i for i in Category.objects.filter(name__in=list_name).all()]

        self.assertEqual(list_assert, result)

    mock_respond = {"products":
                    [
                        {"product_name": "test1",
                         "categories_tags": ["category1"]},
                        {"generic_name": "test2",
                         "categories_tags": ["category2"]},
                        {"categories_tags": ["category3"]}
                    ]}

    @patch('product.management.commands.sample.Request.db_sample_request',
           return_value=mock_respond)
    def test_handle(self, mock_request):
        Command().handle()
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, "test1")

        product = Product.objects.get(id=2)
        self.assertEqual(product.name, "test2")

        category = Category.objects.get(name="category3").name
        self.assertEqual(category, "category3")
