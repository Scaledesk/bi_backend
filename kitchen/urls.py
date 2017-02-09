from django.conf.urls import url, include
from kitchen.views import *

urlpatterns = [
    # url(r'^test/', Test, name='test'),
    url(r'^kitchen-info/', KitchenInfo, name='kitchen_info'),
    url(r'^kitchen-guide', KitchenGuide, name='kitchen_guide'),
    url(r'^reload-flex', ReloadFlex, name='reload_flex'),
    url(r'^reload-kitchen-type', ReloadKitchenType, name='reload-kitchen-type'),
    url(r'^product-consultation', ProductConsultation, name='kitchen_consultation'),
    # url(r'^kitchen-response', KitchenResponse, name='kitchen-response'),
    url(r'^(?P<k_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/(?P<kitchen_slug>[-\w]+)/$', ServeProduct),
    url(r'^(?P<k_type_slug>[-\w]+)/(?P<theme_slug>[-\w]+)/$', ServeKitchen),
    url(r'^(?P<k_type_slug>[-\w]+)/$', ServeTheme),
    url(r'^$', ServeType, name='kitchen')
]
