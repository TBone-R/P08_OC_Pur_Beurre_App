from django.shortcuts import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Label(models.Model):
    name = models.CharField(max_length=200)


class Origin(models.Model):
    name = models.CharField(max_length=200)


class Store(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    nova = models.IntegerField()
    nutri_score = models.CharField(max_length=1)
    label_score = models.IntegerField(default=0)
    image_url = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    labels = models.ManyToManyField(Label, related_name='products', blank=True)
    origins = models.ManyToManyField(Origin, related_name='products', blank=True)
    stores = models.ManyToManyField(Store, related_name='products', blank=True)

    def get_absolute_url(self):
        return reverse("product:product", kwargs={"id": self.id})

    def get_substitute_url(self):
        return reverse("product:substitutes", kwargs={"id": self.id})
