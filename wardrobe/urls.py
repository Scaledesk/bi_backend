from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^(?P<type>\d+)/', ServeType),
    url(r'^(?P<id>\d+)/', ServeProduct),
    # url(r'(?P<id>\d+)', ServeProduct),


    # url(r'^asdf/', asdf),
    # url(r'^kitchen/', include('kitchen.urls')),
    # # url(r'^wardrobe/', include('wardrobe.urls')),
    # url(r'^admin/', admin.site.urls),
]
