from django.conf.urls import url, include
# from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^(?P<type>\d+)/', ServeType),
    url(r'^(?P<id>\d+)/', ServeProduct),
]
