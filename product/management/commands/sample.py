from django.core.management.base import BaseCommand
from constant import OOF_KEY_KEPT
from product.api_off import Request
from product.models import Product, Category


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
        Product.objects.filter(substitutes__isnull=True).filter(originals__isnull=True).delete()
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
            nutrient_levels = product_db.get("nutrient_levels")
            salt = None if not nutrient_levels else nutrient_levels.get("salt")
            sugars = None if not nutrient_levels else \
                nutrient_levels.get("sugars")
            saturated = None if not nutrient_levels else\
                nutrient_levels.get("saturated-fat")
            fat = None if not nutrient_levels else nutrient_levels.get("fat")

            url = product_db.get("url")
            image_url = product_db.get("image_url")

            categories = product_db.get("categories_tags")
            labels = product_db.get("labels_tags")
            # origins = product_db.get("origins_tags")
            # stores = product_db.get("stores")

            new_product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    "name": name,
                    "brand": brand if brand else "",
                    "nova": int(nova) if nova else 0,
                    "nutri_score": nutri_score if nutri_score else "",
                    "url": url if url else "",
                    "image_url": image_url if image_url else "",
                    "salt": salt if salt else "inconnu",
                    "sugars": sugars if sugars else "inconnu",
                    "saturated": saturated if saturated else "inconnu",
                    "fat": fat if fat else "inconnu",
                }

            )

            if created:

                list_many_to_many = [
                    (categories, Category)
                ]

                for request_and_object in list_many_to_many:

                    list_to_save = self.save_many_to_many(*request_and_object)

                    if list_to_save:

                        if request_and_object[0] == categories:
                            for item in list_to_save:
                                new_product[0].categories.add(item)

                try:
                    new_product[0].label_score = len(labels)
                except TypeError:
                    new_product[0].label_score = 0

                new_product[0].save()
