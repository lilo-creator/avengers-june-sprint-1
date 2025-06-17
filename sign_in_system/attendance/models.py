from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.check_in.strftime('%Y-%m-%d %H:%M:%S')}"
    