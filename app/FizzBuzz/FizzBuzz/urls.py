"""fizzbuzz URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers

from FizzBuzz.views import FizzBuzzViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]