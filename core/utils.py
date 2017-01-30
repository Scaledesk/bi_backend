from core.models import *
# from pprint import pprint

def AppendBasicContext(context):
    """ To create common context which will be used in all templates (mainly in header and footer) """
    context['k_types'] = KType.objects.all()
    context['w_types'] = WType.objects.all()
    return context
