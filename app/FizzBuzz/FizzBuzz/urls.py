"""fizzbuzz URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from FizzBuzz.views import FizzBuzzViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]