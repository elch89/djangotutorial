from datetime import datetime
from django.db import models

class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    provider_name = models.CharField(max_length=100, blank=True, null=True)
    provider_email = models.CharField(max_length=3000, blank=True, null=True)
    provider_link = models.CharField(max_length=3000, blank=True, null=True)
    available_coupons = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    description_extended = models.CharField(max_length=3000, blank=True, null=True)
    price_before = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    discount = models.CharField(max_length=5, blank=True, null=True)
    is_after_birth = models.IntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=256, blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True, default=datetime.now)

    class Meta:
        db_table = 'coupons'
        managed = False
