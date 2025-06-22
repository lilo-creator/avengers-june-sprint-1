from django.test import TestCase
from users.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_create_community_user(self):
        user = CustomUser.objects.create_user(username='comm_user', password='test123', user_type='community')
        self.assertEqual(user.username, 'comm_user')
        self.assertEqual(user.user_type, 'community')
        self.assertTrue(user.check_password('test123'))

    def test_create_staff_user(self):
        user = CustomUser.objects.create_user(username='staff_user', password='test123', user_type='staff')
        self.assertEqual(user.username, 'staff_user')
        self.assertEqual(user.user_type, 'staff')
        self.assertTrue(user.check_password('test123'))

