from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from product.models import Product
from constant import ORDER_BY


class CustomUserManager(UserManager):

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    username = models.CharField(
        'username',
        max_length=150,
        unique=False,
    )
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="substitutes")
    original_product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                         related_name="originals")
