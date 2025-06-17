from django.urls import path
from .views import CheckOutView, CheckInView


urlpatterns = [
    path('check-in/', CheckInView.as_view(), name='check_in'),
    path('check-out/', CheckOutView.as_view(), name='check_out'),
]



