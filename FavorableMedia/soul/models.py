from contextlib import contextmanager
from collections import namedtuple
from decimal import Decimal
import datetime
import re
import os
import decimal
import copy
import inspect
import calendar
import json
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from django.db import models
from django.contrib.auth.models import User, Group


class SoulBase(models.Model):
    created_on = models.DateTimeField(editable=False,
                                      default=datetime.datetime.now())
    updated_on = models.DateTimeField(editable=False,
                                      default=datetime.datetime.now())
    created_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_updated_by")

    class Meta:
        abstract = True
