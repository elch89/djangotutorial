from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import AppVersionSerializer
from ..services import AppVersionService

class AppVersionView(APIView):

    def get(self, request, platform=None):
        if platform:
            version = AppVersionService.get_version_by_platform(platform)
            if version:
                serializer = AppVersionSerializer(version)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"detail": "Version not found."}, status=status.HTTP_404_NOT_FOUND)

        versions = AppVersionService.get_all_versions()
        serializer = AppVersionSerializer(versions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppVersionSerializer(data=request.data)
        if serializer.is_valid():
            AppVersionService.create_version(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, platform):
        version = AppVersionService.get_version_by_platform(platform)
        if not version:
            return Response({"detail": "Version not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppVersionSerializer(version, data=request.data, partial=True)
        if serializer.is_valid():
            AppVersionService.update_version(platform, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, platform):
        version = AppVersionService.get_version_by_platform(platform)
        if not version:
            return Response({"detail": "Version not found."}, status=status.HTTP_404_NOT_FOUND)

        AppVersionService.delete_version(platform)
        return Response(status=status.HTTP_204_NO_CONTENT)
