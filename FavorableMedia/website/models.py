from __future__ import unicode_literals

from soul.models import SoulBase
from django.db import models

# Create your models here.


class Blog(SoulBase):
    active = models.BooleanField(default=True, blank=True)
    title = models.CharField(blank=True, null=True, max_length=300)
    url = models.CharField(blank=True, null=True, max_length=300)
    image_link = models.CharField(blank=True, null=True, max_length=300)
