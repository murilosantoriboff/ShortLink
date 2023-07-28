from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=100, unique=True)
    time_date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.original_url