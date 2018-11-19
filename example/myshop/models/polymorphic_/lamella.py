# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from ..discount import Discount
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
        help_text=_("Lammelas width")
    )

    length = models.CharField(
        _("Lamella's length"),
        max_length=25,
        blank=True,
    )

    depth = models.CharField(
        _("Lamella's depth"),
        max_length=25,
        blank=True,
    )

    weight = models.CharField(
        _('weight'),
        default=1,
        max_length=6,
        help_text=_("Weight of item")
    )



    discont_scheme = models.ForeignKey(Discount, blank=True, on_delete=models.CASCADE)

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

    def get_rebate(self, x):
        some_str = self.discont_scheme.discont_scheme.split("\r\n")
        x = int(x)
        temp_discont = 0
        for i in some_str:
            discont = i.split(":")
            num = int(discont[0]) #get first element of tuple for get quantity in db
            if x>=num:
                temp_discont = int(discont[1])
            elif x<=num:
                return temp_discont
        return temp_discont
