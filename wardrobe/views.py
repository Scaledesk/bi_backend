from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from core.models import *
from core.utils import *
from pprint import pprint


# def Test(request):
#     """ view to testing  only"""
#     return render(request, 'privacypolicy.html', None)

def ServeType(request):
    """ view to serve page containing wardrobe types """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'wardrobe/product_types.html', context)

def ThemeContextCreator(w_type_slug):
    """ to create context data for serving theme """
    context = {}
    w_type = WType.objects.get(slug=w_type_slug)
    context['current_w_type']= w_type
    context['themes'] = WTheme.objects.filter(w_type=w_type)
    return context

def ServeTheme(request, w_type_slug):
    """ to serve theme data """
    context = ThemeContextCreator(w_type_slug)
    context = AppendBasicContext(context)
    return render(request, 'wardrobe/product_by_type.html', context)

def WardrobeContextCreator(w_type_slug, theme_slug):
    """ to serves list of wardrobe theme of a particular type """
    context = {}
    wardrobes = []
    w_images = []
    #theme slug is not unique. Its unique together with other attributes
    w_type = WType.objects.get(slug=w_type_slug)
    theme = WTheme.objects.get(w_type=w_type, slug=theme_slug)
    w_list = Wardrobe.objects.filter(theme=theme)
    for wardrobe in w_list:
        temp = wardrobe.__dict__
        temp['image'] = WImage.objects.filter(wardrobe=wardrobe).first().image.url
        wardrobes.append(temp)
    context['wardrobes'] = wardrobes
    return context

def ServeWardrobe(request, w_type_slug, theme_slug):
    """ to serve wardrobes on basis of type and theme """
    context = None
    context = WardrobeContextCreator(w_type_slug, theme_slug)
    context = AppendBasicContext(context)
    return render(request, 'wardrobe/product_by_theme.html', context)

def ProductContextCreator(w_type_slug, theme_slug, wardrobe_slug):
    """ to create context to serve final product """
    context = {}
    w_type = WType.objects.get(slug=w_type_slug)
    # theme slug and wardrobe slug are not unique. they are unique together with other fields
    theme = WTheme.objects.get(w_type=w_type, slug=theme_slug)
    wardrobe = Wardrobe.objects.get(theme=theme, slug=wardrobe_slug)

    w_images = WImage.objects.filter(wardrobe=wardrobe)
    w_material = WMaterial.objects.all()
    w_finishing = WFinishing.objects.all()
    w_appliance = WAppliance.objects.filter(wardrobe=wardrobe)
    w_appliances = WAppliance.objects.filter(wardrobe=wardrobe)

    w_includes = []
    if WIncludes.objects.filter(wardrobe=wardrobe):
        wi_list = WIncludes.objects.filter(wardrobe=wardrobe)
        for obj in wi_list:
            temp = obj.__dict__
            temp['image'] = obj.image.url
            temp['ki_sub'] = WISub.objects.filter(w_includes = obj)
            w_includes.append(temp)

    context['wardrobe'] = wardrobe
    context['w_images'] = w_images
    context['w_material'] = w_material
    context['w_finishing'] = w_finishing
    context['w_includes'] = w_includes
    context['w_appliances'] = w_appliances
    return context

def ServeProduct(request, w_type_slug, theme_slug, wardrobe_slug):
    """ to serve final product based on type, theme and wardrobe """
    context = ProductContextCreator(w_type_slug, theme_slug, wardrobe_slug)
    context = AppendBasicContext(context)
    return render(request, 'wardrobe/wardrobe_pdp.html', context=context)
