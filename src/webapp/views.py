from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from webapp.models.fizzbuzz import FizzBuzz
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from src.webapp.serializers import FizzBuzzSerializer


class FizzBuzzViewSet(viewsets.ModelViewSet):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    @detail_route(methods=['post'])
    def set_user_agent(self, request, pk=None):
        user_agent_string = request.META['HTTP_USER_AGENT']


def site_logout(request):
    logout(request)
    return redirect("index")
