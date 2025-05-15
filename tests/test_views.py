# yoldot/tests/test_user_view.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from yoldot.models import User

# Initialize the APIClient
client = APIClient()

@pytest.mark.django_db
def test_create_user():
    """Test user creation via POST request."""
    url = reverse('user-list')
    payload = {
        "email": "example@test.com",
        "push_agreement": True,
        "push_token": "token123",
        "estimated_birth": "2025-12-25",
        "classification": "Basic",
        "status": "Active",
        "access_token": "access-token-456"
    }
    response = client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["email"] == "example@test.com"
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_get_user():
    """Test retrieving a user."""
    user = User.objects.create(
        email="example2@test.com",
        push_agreement=True,
        push_token="token456",
        estimated_birth="2025-12-25",
        classification="Basic",
        status="Active",
        access_token="access-token-789"
    )
    url = reverse('user-detail', args=[user.id])
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "example2@test.com"

@pytest.mark.django_db
def test_update_user():
    """Test updating a user."""
    user = User.objects.create(
        email="example3@test.com",
        push_agreement=True,
        push_token="token789",
        estimated_birth="2025-12-25",
        classification="Basic",
        status="Active",
        access_token="access-token-101"
    )
    url = reverse('user-detail', args=[user.id])
    payload = {
        "email": "example3-updated@test.com"
    }
    response = client.put(url, payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data["email"] == "example3-updated@test.com"

@pytest.mark.django_db
def test_delete_user():
    """Test deleting a user."""
    user = User.objects.create(
        email="example4@test.com",
        push_agreement=True,
        push_token="token999",
        estimated_birth="2025-12-25",
        classification="Basic",
        status="Active",
        access_token="access-token-111"
    )
    url = reverse('user-detail', args=[user.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert User.objects.count() == 0
