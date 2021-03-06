# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import admin

from shop.admin.defaults import customer
from shop.admin.defaults.order import OrderAdmin
from shop.models.defaults.order import Order
from shop.admin.order import PrintOrderAdminMixin
from shop.admin.delivery import DeliveryOrderAdminMixin

from . import manufacturer

if settings.SHOP_TUTORIAL in ['i18n_polymorphic', 'polymorphic']:
        class OrderAdmin(PrintOrderAdminMixin, DeliveryOrderAdminMixin, OrderAdmin):
            pass

admin.site.register(Order, OrderAdmin)

if settings.SHOP_TUTORIAL == 'polymorphic':
    from . import polymorphic_

elif settings.SHOP_TUTORIAL == 'i18n_polymorphic':
    from . import i18n_polymorphic


__all__ = ['commodity', 'customer']

admin.site.site_header = "Django-SHOP administration"
