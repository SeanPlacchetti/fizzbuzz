from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.site_login, name='login'),
    url(r'^logout$', views.site_logout, name='logout'),
    url(r'^fizzbuzz$', views.FizzBuzzViewSet, name='logout'),
]