from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import staff_member_required
from attendance.models import Attendance
from django.db.models import Count

@staff_member_required
def staff_dashboard(request):
    total_checkins = Attendance.objects.count()
    attendances = Attendance.objects.all()
    return render(request, 'users/dashboard.html', {
        'total_checkins': total_checkins,
        'attendances': attendances
    })