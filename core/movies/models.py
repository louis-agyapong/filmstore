from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class Movie(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    year = models.PositiveSmallIntegerField(_("Year"), blank=True, null=True)
    tags = TaggableManager(_("Tags"), blank=True)

    def __str__(self) -> str:
        return self.name
