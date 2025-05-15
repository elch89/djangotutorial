from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import get_all_hashvaot

class HashvaaView(APIView):
    def get(self, request):
        """Get all hashvaot, grouped by category."""
        hashvaot = get_all_hashvaot()
        if not hashvaot:
            return Response({"message": "No records found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({'data': hashvaot}, status=status.HTTP_200_OK)
