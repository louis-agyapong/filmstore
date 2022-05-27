from email import charset
from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(_("Name"), max_length=256)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=256)
    ratings = models.PositiveBigIntegerField(_("Ratings"))
    author = models.ForeignKey(
        "book.Author",
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self):
        return self.title
