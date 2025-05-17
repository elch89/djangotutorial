from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import get_all_surveys, save_temp_json
from ..serializers import SurveySerializer

class SurveyView(APIView):
    """For admin panel-> implement paging and get"""
    # def get(self,request):
    #     surveys = get_all_surveys()
    #     if not surveys:
    #         return Response({"message": "No records found."}, status=status.HTTP_404_NOT_FOUND)
    #     return Response(surveys, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        
        # Save temp backup
        file_path = save_temp_json(data)
        print(f"Backup created at: {file_path}")

        # Proceed to save in DB...
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)