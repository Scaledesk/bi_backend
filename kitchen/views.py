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

def ServeType(request):
    context = {}
    context['k_types'] = KType.objects.all()
    return render(request, 'kitchen/product_types.html', context)

def ThemeContextCreator(k_type_slug):
    context = {}
    pprint(type(k_type_slug))
    k_type = KType.objects.get(slug=k_type_slug)
    context['k_type']= k_type
    context['themes'] = KTheme.objects.filter(k_type=k_type)
    return context

def ServeTheme(request, k_type_slug):
    context = ThemeContextCreator(k_type_slug)
    return render(request, 'kitchen/product_by_type.html', context)


def KitchenContextCreator(k_type_slug, theme_slug):
    context = {}
    #theme slug is not unuque. Its unique together with other attributes
    k_type = KType.objects.get(slug=k_type_slug)
    theme = KTheme.objects.get(k_type=k_type, slug=theme_slug)
    kitchens = Kitchen.objects.filter(theme=theme)
    context['kitchens'] = kitchens
    return context

def ServeKitchen(request, k_type_slug, theme_slug):
    context = None
    context = KitchenContextCreator(k_type_slug, theme_slug)
    return render(request, 'kitchen/product_by_theme.html', context)

def ProductContextCreator(k_type_slug, theme_slug, kitchen_slug):
    context = {}
    k_type = KType.objects.get(slug=k_type_slug)
    # theme slug and kitchen slug are not unique. they are unique together with other fields
    theme = KTheme.objects.get(k_type=k_type, slug=theme_slug)
    kitchen = Kitchen.objects.get(theme=theme, slug=kitchen_slug)

    k_images = KImage.objects.filter(kitchen=kitchen)
    k_material = KMaterial.objects.all()
    k_finishing = KFinishing.objects.all()
    k_appliance = KAppliance.objects.filter(kitchen=kitchen)
    k_includes = KIncludes.objects.filter(kitchen=kitchen)

    context['kitchen'] = kitchen
    context['k_images'] = k_images
    context['k_material'] = k_material
    context['k_finishing'] = k_finishing
    context['k_includes'] = k_includes

    return context

def ServeProduct(request, k_type_slug, theme_slug, kitchen_slug):
    context = ProductContextCreator(k_type_slug, theme_slug, kitchen_slug)
    return render(request, 'kitchen/kitchen_pdp.html', context=context)

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
