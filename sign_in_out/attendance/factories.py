import factory
from django.contrib.auth.models import User
from .models import Attendance
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')
    password = factory.Faker('password')

class AttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance
    user = factory.SubFactory(UserFactory)
    check_in = factory.Faker('date_time_this_month')
    