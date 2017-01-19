from django.conf.urls import url, include
from kitchen.views import *

urlpatterns = [
    # url(r'^test/', Test, name='test'),
    url(r'^(?P<k_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/(?P<kitchen_slug>[-\w]+)/$', ServeProduct),
    url(r'^(?P<k_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/$', ServeKitchen),
    url(r'^(?P<k_type_slug>[-\w]+)/$', ServeTheme),
    url(r'^$', ServeType, name='kitchen')
]
