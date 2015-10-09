from rest_framework import serializers
from webapp.models.fizzbuzz import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
