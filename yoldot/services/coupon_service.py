from ..models import Coupon

class CouponService:
    @staticmethod
    def get_all_coupons():
        """Fetch all coupons from the database."""
        return Coupon.objects.all()

    @staticmethod
    def get_coupon_by_id(coupon_id):
        """Fetch a single coupon by ID."""
        try:
            return Coupon.objects.get(id=coupon_id)
        except Coupon.DoesNotExist:
            return None

    @staticmethod
    def create_coupon(data):
        """Create a new coupon entry."""
        return Coupon.objects.create(**data)

    @staticmethod
    def update_coupon(coupon_id, data):
        """Update an existing coupon entry."""
        coupon = CouponService.get_coupon_by_id(coupon_id)
        if coupon:
            for key, value in data.items():
                setattr(coupon, key, value)
            coupon.save()
            return coupon
        return None

    @staticmethod
    def delete_coupon(coupon_id):
        """Delete a coupon by ID."""
        coupon = CouponService.get_coupon_by_id(coupon_id)
        if coupon:
            coupon.delete()
            return True
        return False
