from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields


# ==============================================================================
# Product Categories
# ==============================================================================
class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


# ==============================================================================
# Maker
# ==============================================================================
class Maker(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


# ==============================================================================
# Product
# ==============================================================================
class Product(models.Model):
    # Currency
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish Crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        EURO = ("EUR", _("Euro"))
        POUND_STERLING = ("GBP", _("Pound Sterling"))
        YEN = ("JPY", _("Yen"))
        AUSTRALIAN_DOLLAR = ("AUD", _("Australian Dollar"))

    # name
    name = models.CharField(max_length=512)
    # subtitle
    subtitle = models.CharField(max_length=512)
    # maker
    maker = models.ForeignKey(
        Maker,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    # images
    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)
    # price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    # currency
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )
    # Variation Products Ids
    variation_products_ids = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.subtitle} - {self.maker}"
