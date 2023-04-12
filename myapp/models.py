from django.db import models

class URL(models.Model):
    url = models.URLField(max_length=200)
    status_code = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.url
