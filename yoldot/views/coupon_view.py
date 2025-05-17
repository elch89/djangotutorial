from rest_framework import generics
from ..serializers import CouponSerializer
from ..services import CouponService
from rest_framework.response import Response
from rest_framework import status

class CouponListView(generics.ListCreateAPIView):
    queryset = CouponService.get_all_coupons()
    serializer_class = CouponSerializer

    def post(self, request, *args, **kwargs):
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            CouponService.create_coupon(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CouponSerializer

    def get_object(self):
        coupon_id = self.kwargs.get('pk')
        return CouponService.get_coupon_by_id(coupon_id)

    def put(self, request, *args, **kwargs):
        coupon = self.get_object()
        if coupon:
            serializer = CouponSerializer(coupon, data=request.data)
            if serializer.is_valid():
                CouponService.update_coupon(coupon.id, serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Coupon not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        coupon = self.get_object()
        if coupon:
            CouponService.delete_coupon(coupon.id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Coupon not found"}, status=status.HTTP_404_NOT_FOUND)
