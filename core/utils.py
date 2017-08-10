from core.models import *
# from pprint import pprint

def AppendBasicContext(context):
    """ To create common context which will be used in all templates (mainly in header and footer) """
    context['k_types'] = KType.objects.all()
    context['w_types'] = WType.objects.all()
    context['meta_title'] = 'Bloom Interio'
    context['meta_desc'] = 'Bloom Interio - Modular Kitchen, Modern Wardrobes & Wardrobes Design Manufacturer from Gurgaon, Haryana, India'
    context['meta_keyword'] = 'Modular Kitchen, Modern Wardrobes, Wardrobes Design, Italian Modular Kitchens, Island Modular Kitchen, Wooden Modular Kitchen, Modular Kitchen, Bloom Interio, Gurgaon'
    return context
