from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import get_all_surveys

class SurveyView(APIView):
    def get(self,request):
        surveys = get_all_surveys()
        if not surveys:
            return Response({"message": "No records found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(surveys, status=status.HTTP_200_OK)