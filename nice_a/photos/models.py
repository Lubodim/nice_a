from django.core.validators import MinLengthValidator
from django.db import models

from nice_a.pets.models import Pet
from nice_a.photos.validators import validate_file_less_then_5mb


# Create your models here.

class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photo/',
        null=False,
        blank=False,
        validators=(validate_file_less_then_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
                    ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    def __str__(self):
        return f"{self.description} - ({self.publication_date})"