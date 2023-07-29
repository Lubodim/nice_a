from enum import unique

from django.db import models
from django.utils.text import slugify
from nice_a.core.model_mixin import StrFormFieldsMixin


# Create your models here.

class Pet(StrFormFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.name}")
        return super().save(*args, **kwargs)
