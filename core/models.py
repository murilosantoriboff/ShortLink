from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField()

    def __str__(self) -> str:
        return self.original_url