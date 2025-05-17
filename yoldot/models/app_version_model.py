from datetime import date
from django.db import models

class AppVersion(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=10)
    version = models.CharField(max_length=10)
    release_date = models.DateField(default=date.today)

    class Meta:
        db_table = 'app_versions'
        managed = False
