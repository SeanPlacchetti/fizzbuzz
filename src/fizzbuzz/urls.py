"""fizzbuzz URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import detail_route

from .models import FizzBuzz


class FizzBuzzSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FizzBuzz


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class FizzBuzzViewSet(viewsets.ModelViewSet):
    queryset = FizzBuzz.objects.all()
    serializer_class = FizzBuzzSerializer

    @detail_route(methods=['post'])
    def set_user_agent(self, request, pk=None):
        user_agent_string = request.META['HTTP_USER_AGENT']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]