from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def check_in_page(request):
    return render(request, 'attendance/check_in.html')
