from django.conf.urls import url, include
from wardrobe.views import *

urlpatterns = [
    # url(r'^test/', Test, name='test'),
    url(r'^(?P<w_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/(?P<wardrobe_slug>[-\w]+)/$', ServeProduct),
    url(r'^(?P<w_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/$', ServeWardrobe),
    url(r'^(?P<w_type_slug>[-\w]+)/$', ServeTheme),
    url(r'^$', ServeType, name='wardrobe')
]
