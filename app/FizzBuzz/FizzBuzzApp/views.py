from django.contrib.auth.models import User
from rest_framework import viewsets

from FizzBuzzApp.models import FizzBuzz
from FizzBuzzApp.serializers import FizzBuzzSerializer, UserSerializer

__author__ = 'seanplacchetti'


# ViewSets define the view behavior.
class FizzBuzzViewSet(viewsets.ModelViewSet):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    def perform_create(self, serializer):
        serializer.save(user_agent=self.request.META['HTTP_USER_AGENT'])


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
