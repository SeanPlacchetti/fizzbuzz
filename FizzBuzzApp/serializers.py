from rest_framework import serializers
from FizzBuzzApp.models import FizzBuzz
from django.contrib.auth.models import User

__author__ = 'seanplacchetti'


class FizzBuzzSerializer(serializers.HyperlinkedModelSerializer):
    fizzbuzz_id = serializers.IntegerField(source='id', read_only=True)
    creation_date = serializers.DateTimeField(source='created_at', read_only=True)
    useragent = serializers.CharField(source='user_agent', read_only=True)
    class Meta:
        model = FizzBuzz
        fields = ('fizzbuzz_id', 'creation_date', 'useragent', 'message' )


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
