from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.db.models import Q
from core.models import *

class StaticViewSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return ['landing', 'kitchen','wardrobe','about','faq','contact']

    def location(self, item):
        return reverse(item)

class KitchenSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return Kitchen.objects.all()

class KitchenTypeSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return KType.objects.all()

class WardrobeSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return Wardrobe.objects.all()

class WardrobeTypeSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return WType.objects.all()
