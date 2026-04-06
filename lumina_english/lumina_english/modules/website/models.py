from django.db import models

from djangocms_frontend.models import AbstractFrontendUIItem
from django.utils.translation import gettext_lazy as _

class LuminaFrontendBaseModel(AbstractFrontendUIItem):
    class Meta:
        abstract = False