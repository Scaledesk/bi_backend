from django.conf.urls import url, include
from wardrobe.views import *

urlpatterns = [
    # url(r'^test/', Test, name='test'),
    url(r'^reload-flex', ReloadFlex, name='reload_flex'),
    url(r'^product-consultation', ProductConsultation, name='wardrobe_consultation'),
    # url(r'^wardrobe-response', WardrobeResponse, name='wardrobe-response'),
    # url(r'^(?P<w_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/(?P<wardrobe_slug>[-\w]+)/$', ServeProduct),
    # url(r'^(?P<w_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/$', ServeWardrobe),
    url(r'^(?P<w_type_slug>[-\w]+)/(?P<wardrobe_slug>[-\w]+)/$', ServeProduct),
    url(r'^(?P<w_type_slug>[-\w]+)/$', ServeWardrobe), #ServeTheme
    url(r'^$', ServeWardrobeInfo, name='wardrobe'),
    url(r'^guid-info$', ServeType, name='wardrobe-guid')
]
