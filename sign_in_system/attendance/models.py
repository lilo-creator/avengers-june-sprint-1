from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} check in at  {self.check_in.date() if self.check_in else 'N/A'} - check out at {self.check_out.date() if self.check_out else 'N/A'}"