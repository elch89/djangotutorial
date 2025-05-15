# yoldot/services/user_service.py
from ..models import User
from ..serializers import UserSerializer

def get_user_by_id(user_id): # Not part of original class
    user = User.objects.filter(id=user_id).first()
    if user:
        return UserSerializer(user)
    return None
def get_user_by_email(email): # findUser($email)
    user = User.objects.filter(email=email).first()
    if user:
        return UserSerializer(user)
    return None
def get_all_users(): # getUserData()
    users = User.objects.all()
    return UserSerializer(users, many=True)

def create_user(data): # createUser($data)
    """Create a new user instance - saving is done in the view."""
    return UserSerializer(data=data)

def update_user(email, data):
    user = User.objects.filter(email=email).first()
    if not user:
        return None
    serializer = UserSerializer(user, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer
    return serializer

def delete_user(email): # deleteUser($email)
    user = User.objects.filter(email=email).first()
    if user:
        user.delete()
        return True
    return False
