from django.db import models
from django.contrib.auth.models import User

from product.models import Product
from constant import ORDER_BY


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_by_1 = models.CharField(
        max_length=11,
        choices=ORDER_BY,
        default="name",
    )
    order_by_2 = models.CharField(
        max_length=11,
        choices=ORDER_BY,
        default="nova",
    )
    order_by_3 = models.CharField(
        max_length=11,
        choices=ORDER_BY,
        default="nutri_score",
    )
    order_by_4 = models.CharField(
        max_length=11,
        choices=ORDER_BY,
        default="label_score",
    )


class SavedSubstitute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="substitutes")
    original_product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                         related_name="originals")
