from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from core.models import *
from pprint import pprint
#
# def ProductContextCreator(id):
#     p = Kitchen.objects.get(id=id)
#
#
#

def Test(request):
    return render(request, 'privacypolicy.html', None)

# def ProductContextCreator(kitchen):
#     context = {}
#     context['kitchen'] =  kitchen.__dict__
#     context['KIncludes'] = None
#     context['KAppliance'] = None
#     context['KMaterial'] = None
#     context['KColor'] = None
#     context['KImage'] = None
#
#     if KIncludes.objects.filter(kitchen=kitchen).exists():
#         list = []
#         obj_list = KIncludes.objects.filter(kitchen=kitchen)
#         for obj in obj_list:
#             list.append(obj.__dict__)
#         context['KIncludes'] = list
#
#     if KAppliance.objects.filter(kitchen=kitchen).exists():
#         list = []
#         obj_list = KAppliance.objects.filter(kitchen=kitchen)
#         for obj in obj_list:
#             list.append(obj.__dict__)
#         context['KAppliance'] = list
#
#     if KMaterial.objects.all().exists():
#         list = []
#         obj_list = KMaterial.objects.all()
#         for obj in obj_list:
#             list.append(obj.__dict__)
#         context['KMaterial'] = list
#
#     if KColor.objects.all().exists():
#         list = []
#         obj_list = KColor.objects.all()
#         for obj in obj_list:
#             list.append(obj.__dict__)
#         context['KColor'] = list
#
#     if KImage.objects.filter(kitchen=kitchen).exists():
#         list = []
#         obj_list = KImage.objects.filter(kitchen=kitchen)
#         for obj in obj_list:
#             list.append(obj.__dict__)
#         context['KImage'] = list
#     return context

def KitchenContextCreator(type):
    context = {}
    if KTypes.objects.filter(name=type).exists():
        context['kitchen'] =  Kitchen.objects.filter(type=KTypes.objects.get(name=type))
    return context

def ProductContextCreator(kitchen):
    context = {}
    context['kitchen'] =  kitchen
    context['KIncludes'] = None
    context['KAppliance'] = None
    context['KMaterial'] = None
    context['KMaterial'] = None
    context['KColor'] = None
    context['KImage'] = None

    if KIncludes.objects.filter(kitchen=kitchen).exists():
        context['KIncludes'] = KIncludes.objects.filter(kitchen=kitchen)
    if KAppliance.objects.filter(kitchen=kitchen).exists():
        context['KAppliance'] = KAppliance.objects.filter(kitchen=kitchen)
    if KMaterial.objects.all().exists():
        context['KMaterial'] = KMaterial.objects.all()
    if KFinishing.objects.all().exists():
        context['KFinishing'] = KFinishing.objects.all()
    if KColor.objects.all().exists():
        context['KColor'] = KColor.objects.all()
    if KImage.objects.filter(kitchen=kitchen).exists():
        context['KImage'] = KImage.objects.filter(kitchen=kitchen)
    return context

def ServeKitchen(request, type):
    context = None
    context = KitchenContextCreator(typ)
    return HttpResponse(context)

def ServeType(request):
    context = None
    # context = TypeContextCreator

def ServeProduct(request, type, name):
    kitchen = Kitchen.objects.get(type=KType.objects.get(name=type), name=name)
    context = ProductContextCreator(kitchen)
    return render(request, 'kitchen/kitchen_pdp.html', context=context)
