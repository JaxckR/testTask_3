from django.db import models


class RegionHistory(models.Model):
    region = models.CharField(max_length=255, unique=True, blank=False, null=False)
    count = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return f"{self.region} - {self.count}"