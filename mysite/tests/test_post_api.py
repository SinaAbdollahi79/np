import pytest 
from rest_framework.test import APIClient
from django.urls import reverse

class TestPostApi :
    def test_get_post_respons_200_status(self):
        client = APIClient()
        url = reverse('mysite:api-v1:post-list')
        response = client.get(url)
        assert response.status_code == 200
        