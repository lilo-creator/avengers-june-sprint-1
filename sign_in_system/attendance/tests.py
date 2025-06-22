from rest_framework.test import APITestCase
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from django.urls import reverse

class AttendanceTests(APITestCase):
    def setUp(self):
        # Create community user
        self.user = CustomUser.objects.create_user(
            username='community_user',
            password='pass1234',
            user_type='community'
        )

        # Create token and authenticate
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_community_user_can_check_in(self):
        response = self.client.post('/api/check-in/')
        self.assertEqual(response.status_code, 201)

    def test_community_user_cannot_check_in_twice(self):
        self.client.post('/api/check-in/')
        response = self.client.post('/api/check-in/')
        self.assertEqual(response.status_code, 400)

    def test_community_user_can_check_out(self):
        self.client.post('/api/check-in/')
        response = self.client.post('/api/check-out/')
        self.assertEqual(response.status_code, 200)

    def test_check_out_without_check_in_fails(self):
        response = self.client.post('/api/check-out/')
        self.assertEqual(response.status_code, 400)
