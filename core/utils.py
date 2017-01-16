from core.models import *

def AppendBasicContext(context):
        context['k_types'] = KType.objects.all()
        return context
