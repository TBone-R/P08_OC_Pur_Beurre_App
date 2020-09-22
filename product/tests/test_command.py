from django.test import SimpleTestCase
from product.management.commands.sample import Command


class TestSample(SimpleTestCase):

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
            "image_url": "image_url"
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
            "origins_tags": None,
            "stores": None,
            "labels_tags": None,
            "nova_group": None,
            "nutrition_grade_fr": None,
            "image_url": None
        }, {
            "product_name": None,
            "generic_name": "generic_name",
            "brands_tags": "brands_tags",
            "categories_tags": "categories_tags",
            "origins_tags": "origins_tags",
            "stores": "stores",
            "labels_tags": "labels_tags",
            "nova_group": "nova_group",
            "nutrition_grade_fr": "nutrition_grade_fr",
            "image_url": "image_url"
        }, {
            "product_name": None,
            "generic_name": None,
            "brands_tags": None,
            "categories_tags": None,
            "origins_tags": None,
            "stores": None,
            "labels_tags": None,
            "nova_group": None,
            "nutrition_grade_fr": None,
            "image_url": None
        }]

        self.assertEqual(Command.get_keys(test), result)