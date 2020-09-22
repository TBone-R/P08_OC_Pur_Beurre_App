from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_by_1 = models.CharField(max_length=200)
    order_by_2 = models.CharField(max_length=200)
    order_by_3 = models.CharField(max_length=200)
    order_by_4 = models.CharField(max_length=200)


class SavedSubstitute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="substitutes")
    original_product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                         related_name="originals")
