from django.core.management.base import BaseCommand
from constant import OOF_KEY_KEPT
from product.api_off import Request
from product.models import Product, Label, Store, Category, Origin


class Command(BaseCommand):

    @staticmethod
    def get_keys(products_brut):
        products = \
            [{key: p.get(key) for key in OOF_KEY_KEPT} for p in products_brut]

        return products

    @staticmethod
    def save_many_to_many(list_from_request, db_object):

        if list_from_request:

            list_item = []

            for item in list_from_request:
                item_db = db_object.objects.get_or_create(
                    name=item,
                    defaults={'name': item}, )

                list_item.append(item_db[0])

            return list_item

        else:
            return None

    def handle(self, *args, **kwargs):
        products = Request.db_sample_request()["products"]
        products = self.get_keys(products)

        for product_db in products:

            name = product_db.get("product_name")
            if not name:
                name = product_db.get("generic_name")
                if not name:
                    name = "Unknown"

            brand = product_db.get("product_name")
            nova = product_db.get("nova_group")
            nutri_score = product_db.get("nutrition_grade_fr")
            image_url = product_db.get("image_url")

            categories = product_db.get("categories_tags")
            labels = product_db.get("labels_tags")
            origins = product_db.get("origins_tags")
            stores = product_db.get("stores")

            new_product = Product.objects.get_or_create(
                name=name,
                defaults={
                    "name": name,
                    "brand": brand if brand else "",
                    "nova": int(nova) if nova else 0,
                    "nutri_score": nutri_score if nutri_score else "",
                    "image_url": image_url if image_url else ""
                }

            )

            if new_product[1]:

                list_many_to_many = [
                    (categories, Category),
                    (labels, Label),
                    (origins, Origin),
                    (stores, Store),
                ]

                for request_and_object in list_many_to_many:

                    list_to_save = self.save_many_to_many(*request_and_object)

                    if list_to_save:

                        if request_and_object[0] == categories:
                            for item in list_to_save:
                                new_product[0].categories.add(item)
                        elif request_and_object[0] == labels:
                            for item in list_to_save:
                                new_product[0].label_score = len(list_to_save)
                                new_product[0].labels.add(item)
                        elif request_and_object[0] == origins:
                            for item in list_to_save:
                                new_product[0].origins.add(item)
                        elif request_and_object[0] == stores:
                            for item in list_to_save:
                                new_product[0].stores.add(item)

                new_product[0].save()
