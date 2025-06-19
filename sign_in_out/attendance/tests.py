

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Attendance
from datetime import datetime

class AttendanceTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.attendance = Attendance.objects.create(user=self.user, check_in=datetime.now())

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.user.username, 'testuser')