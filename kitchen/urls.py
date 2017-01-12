from django.conf.urls import url, include
# from django.contrib import admin
from kitchen.views import *

urlpatterns = [
    url(r'^test/', Test, name='test'),
    url(r'^(?P<type>[-\w]+)/$', ServeType),
    url(r'^$', ServeType, name='kitchen')
    # url(r'^(?P<type>[-\w]+)/', ServeTypes),
    # url(r'^(?P<type>[-\w]+)/', ServeNames),
    # url(r'^(?P<type>[-\w]+)/(?P<name>[-\w]+)/$', ServeSizesProduct),
    # url(r'^(?P<type>[-\w]+)/(?P<name>[-\w]+)/$', ServeProduct),
    ## url(r'^kitchen-size/', KitchenSizeView, name='kitchen_size'),
]
# <li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }}
