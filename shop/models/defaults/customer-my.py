# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from shop.models.customer import BaseCustomer


class Customer(BaseCustomer):
    """
    Default materialized model for Customer, adding a customer's number and salutation.

    If this model is materialized, then also register the corresponding serializer class
    :class:`shop.serializers.defaults.customer.CustomerSerializer`.
    """
    number = models.PositiveIntegerField(
        _("Customer Number"),
        null=True,
        default=None,
        unique=True,
    )

    name = models.CharField(_("Full name"), max_length=1024, blank=True)

    phonesnumber = models.CharField(
        _("Phone number"),
        default='+375(29)',
        max_length=25,
        # blank=True,
    )
    def get_number(self):
        return self.number

    def get_or_assign_number(self):
        if self.number is None:
            aggr = Customer.objects.filter(number__isnull=False).aggregate(models.Max('number'))
            self.number = (aggr['number__max'] or 0) + 1
            self.save()
        return self.get_number()
