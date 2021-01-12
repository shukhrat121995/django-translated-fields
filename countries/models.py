from django.db import models
from translated_fields import TranslatedField


class Country(models.Model):
    name = TranslatedField(
        models.CharField(max_length=255, default=None, blank=True)
    )

    def __str__(self):
        return self.name
