# yoldot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import (
    get_user_by_email,
    get_all_users,
    create_user,
    update_user,
    delete_user
)

class UserView(APIView):

    def get(self, request, email=None):
        if email:
            user = get_user_by_email(email)
            if user:
                return Response(user.data, status=status.HTTP_200_OK)
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        users = get_all_users()
        return Response(users.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 🔍 Create the user serializer
        user_serializer = create_user(request.data)
        
        # ✅ Check if it is valid
        if user_serializer.is_valid():
            # ✅ Manually save the user instance
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        # ❌ If not valid, return the errors
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, email):
        user = update_user(email, request.data)
        if user:
            if user.is_valid():
                return Response(user.data, status=status.HTTP_200_OK)
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, email):
        if delete_user(email):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
