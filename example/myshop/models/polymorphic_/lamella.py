# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField

from shop.money.fields import MoneyField

from .product import Product, BaseProductManager


class LamellaFix(Product):
    # common product fields
    unit_price = MoneyField(
        _("Unit price"),
        decimal_places=3,
        help_text=_(" per unit"),
    )
    LAM_WIDTH = (('38', '38 mm'), ('53', '53 mm'), ('63', '63 mm'), ('68', '68 mm'))
    lamella_width = models.CharField(
        _('width'),
        default=53,
        max_length=6,
        choices=LAM_WIDTH,
        db_index=True,
        help_text=_("Lammelas width")
    )

    product_code = models.CharField(
        _("Product code"),
        max_length=255,
        unique=True,
    )
    description = HTMLField(
        verbose_name=_("Description"),
        configuration='CKEDITOR_SETTINGS_DESCRIPTION',
        help_text=_("Full description used in the catalog's detail view of Smart Cards."),
    )

    default_manager = BaseProductManager()

    class Meta:
        verbose_name = _("Lamella")
        verbose_name_plural = _("Lamellas")

    def get_price(self, request):
        return self.unit_price
