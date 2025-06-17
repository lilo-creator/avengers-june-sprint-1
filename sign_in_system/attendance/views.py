from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from django.utils import timezone
from rest_framework import status

class CheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        today = timezone.now().date()
        if Attendance.objects.filter(user=user, date=today).exists():
            return Response({"error": "Already checked in today"}, status=status.HTTP_400_BAD_REQUEST)
        
        attendance = Attendance.objects.create(
            user=user,
            check_in=timezone.now(),
            date=today
        )
        return Response({"message": "Checked in successfully", "check_in": attendance.check_in}, status=status.HTTP_201_CREATED)


class CheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        today = timezone.now().date()
        try:
            attendance = Attendance.objects.get(user=user, date=today, check_out__isnull=True)
            attendance.check_out = timezone.now()
            attendance.save()
            return Response({"message": "Checked out successfully", "check_out": attendance.check_out}, status=status.HTTP_200_OK)
        except Attendance.DoesNotExist:
            return Response({"error": "No check-in record found for today"}, status=status.HTTP_400_BAD_REQUEST)
