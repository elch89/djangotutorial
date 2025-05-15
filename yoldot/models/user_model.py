from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    email = models.CharField(max_length=256, unique=True)  # Unique constraint
    push_agreement = models.BooleanField(default=False)  # `int` -> BooleanField
    push_token = models.CharField(max_length=256, blank=True, null=True)
    estimated_birth = models.CharField(max_length=256, blank=True, null=True)
    classification = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=256, default="unconfirmed")
    access_token = models.CharField(max_length=64, default="0")
    created_at = models.DateTimeField(auto_now_add=True)  # This will match with MySQL timestamp

    class Meta:
        db_table = 'user_data'   # Link to the existing table
        managed = False 
