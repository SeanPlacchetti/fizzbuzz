"""fizzbuzz URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from FizzBuzzApp.views import FizzBuzzViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'fizzbuzz', FizzBuzzViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [url(r'^', include(router.urls)), ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns.append(url(r'^api/', include('rest_framework.urls',
                                             namespace='rest_framework')))
    urlpatterns.append(url(r'^admin/', admin.site.urls))
