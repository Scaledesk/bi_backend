from core.models import *
# from pprint import pprint

def AppendBasicContext(context):
    """ To create common context which will be used in all templates (mainly in header and footer) """
    context['k_types'] = KType.objects.all()
    context['w_types'] = WType.objects.all()
    context['meta_title'] = 'Bloom Interio - Modular Kitchen Manufacturer Delhi, Gurgaon & Noida'
    context['meta_desc'] = 'Bloom Interio provides a range of beautiful modular kitchens, wardrobes & customised furniture to adorn your home interiors. Check modular kitchen price and cost with our price calculator.'
    context['meta_keyword'] = 'modular kitchen price, modular kitchen gurgaon, modular kitchen in gurgaon, modular kitchen manufacturer, modular kitchen cost, modular kitchen dealers, best modular kitchen, cost of modular kitchen, modular kitchen designer, budget modular kitchen'
    return context
