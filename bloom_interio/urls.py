"""bloom_interio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from web.views import *
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap   
from core.custom_sitemap import *
sitemaps = {
    'static': StaticViewSitemap,
    'kitchen': KitchenSitemap,
    'kitchenType':KitchenTypeSitemap,
    'wardrobe': WardrobeSitemap,
    'wardrobeType':WardrobeTypeSitemap
}

urlpatterns = [
    # url(r'^test/', TestView, name='test'),
    url(r'^kitchen/', include('kitchen.urls')),
    url(r'^wardrobe/', include('wardrobe.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^privacy-policy/', PrivacyPolicyView, name='privacy_policy'),
    url(r'^contact/', ContactView, name='contact'),
    url(r'^about/', AboutView, name='about'),
    url(r'^faq/', FAQView, name='faq'),
    # ne page urls
    url(r'^modularkitchen-delhi-ncr/', ServeLandingView, name='modularkitchen-delhi-ncr'),
    url(r'^requestedCallback/', RequestedCallbackView, name='requested-callback'),
    url(r'^freeConsultation/', FreeConsultation, name='free-consultation'),
    url(r'^modular-kitchen-in-gurgaon/', ServeLandingView, name='modular-kitchen-in-gurgaon'),

    url(r'^interior/', InteriorView, name='interior'),
    url(r'^product-help/', ProductHelpView, name='product_help'),
    url(r'^terms-and-conditions/', TermsAndConditionsView, name='terms_and_conditions'),
    url(r'^contact-request/', ContactRequestView, name='contact-request'),
    url(r'^modal-request/$', ModalFormView, name='modal-request'),
    url(r'^thank-you', ThankYouView, name='thank_you'),
    url(r'^modular-kitchen-accessories/', ModularKitchenAccessories, name='modular_accessories'),
    url(r'^$', LandingView, name='landing'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml',content_type='text/xml')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
