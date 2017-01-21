from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from core.models import *
from core.utils import *
from pprint import pprint


# def Test(request):
#     """ view to testing  only"""
#     return render(request, 'privacypolicy.html', None)

def ServeType(request):
    """ view to serve page containing kitchen types """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'kitchen/product_types.html', context)

def ThemeContextCreator(k_type_slug):
    """ to create context data for serving theme """
    context = {}
    pprint(type(k_type_slug))
    k_type = KType.objects.get(slug=k_type_slug)
    context['current_k_type']= k_type
    context['themes'] = KTheme.objects.filter(k_type=k_type)
    return context

def ServeTheme(request, k_type_slug):
    """ to serve theme data """
    context = ThemeContextCreator(k_type_slug)
    context = AppendBasicContext(context)
    return render(request, 'kitchen/product_by_type.html', context)


def KitchenContextCreator(k_type_slug, theme_slug):
    """ to serves list of kitchen them of a particular type """
    context = {}
    kitchens = []
    k_images = []
    #theme slug is not unique. Its unique together with other attributes
    k_type = KType.objects.get(slug=k_type_slug)
    theme = KTheme.objects.get(k_type=k_type, slug=theme_slug)
    k_list = Kitchen.objects.filter(theme=theme)
    for kitchen in k_list:
        temp = kitchen.__dict__
        temp['image'] = KImage.objects.filter(kitchen=kitchen).first().image.url
        kitchens.append(temp)
    context['kitchens'] = kitchens
    return context

def ServeKitchen(request, k_type_slug, theme_slug):
    """ to serve kitchens on basis of type and theme """
    context = None
    context = KitchenContextCreator(k_type_slug, theme_slug)
    context = AppendBasicContext(context)
    return render(request, 'kitchen/product_by_theme.html', context)

def ProductContextCreator(k_type_slug, theme_slug, kitchen_slug):
    """ to create context to serve final product """
    context = {}
    k_type = KType.objects.get(slug=k_type_slug)
    # theme slug and kitchen slug are not unique. they are unique together with other fields
    theme = KTheme.objects.get(k_type=k_type, slug=theme_slug)
    kitchen = Kitchen.objects.get(theme=theme, slug=kitchen_slug)

    k_images = KImage.objects.filter(kitchen=kitchen)
    k_material = KMaterial.objects.all()
    k_finishing = KFinishing.objects.all()
    k_appliance = KAppliance.objects.filter(kitchen=kitchen)
    k_appliances = KAppliance.objects.filter(kitchen=kitchen)

    k_includes = []
    if KIncludes.objects.filter(kitchen=kitchen):
        ki_list = KIncludes.objects.filter(kitchen=kitchen)
        for obj in ki_list:
            temp = obj.__dict__
            temp['image'] = obj.image.url
            temp['ki_sub'] = KISub.objects.filter(k_includes = obj)
            k_includes.append(temp)

    context['kitchen'] = kitchen
    context['k_images'] = k_images
    context['k_material'] = k_material
    context['k_finishing'] = k_finishing
    context['k_includes'] = k_includes
    context['k_appliances'] = k_appliances
    return context

def ReloadFlex(request):
    context={}
    color = request.POST['color']
    k_id = request.POST['k_id']
    flex_images = KImage.objects.filter(kitchen = Kitchen.objects.get(id=id))
    context['flex_images'] = flex_images
    context['color'] = color
    return render(request, 'reload_flex.html', context)

def ServeProduct(request, k_type_slug, theme_slug, kitchen_slug):
    """ to serve final product based on type, theme and kitchen """
    context = ProductContextCreator(k_type_slug, theme_slug, kitchen_slug)
    context = AppendBasicContext(context)
    return render(request, 'kitchen/kitchen_pdp.html', context=context)

def KitchenResponse(request):
    """ to save the response received on kitchen product """
    return HttpResponse(request.POST)

def ProductConsultation(request):
    if request.method == 'POST':
        from django.core.mail import send_mail
        from bloom_interio.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL

        name = request.POST['name']
        contact_no = request.POST['contact_no']
        user_email = request.POST['user_email']
        address = request.POST['address']
        color = str(request.POST['color'])
        finish = request.POST['finish']
        material = request.POST['material']

        kitchen_id = request.POST['kitchen']
        kitchen = Kitchen.objects.get(id=kitchen_id)
        dimension = str(kitchen.l) +'*'+ str(kitchen.b) +'*'+ str(kitchen.h)

        kitchen_theme = kitchen.theme.name
        kitchen_type = kitchen.theme.k_type.name


        subject = 'Custom quote request'
        message = ('Name: ' + name + \
            '\nContact No: ' + contact_no + \
            '\nEmail: '+ user_email + \
            '\nAddress: '+ address + \
            '\nKitchen Type: '+ kitchen_type + \
            '\nKitchen Theme: '+ kitchen_theme + \
            '\nKitchen: '+ kitchen.name + \
            '\nDimension: '+ dimension + \
            '\nMaterial: '+ material + \
            '\nFinish: '+ finish + \
            '\nColor: '+ color)

        if send_mail(subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL]):
            subject = 'Bloom Interio'
            message = ('Hi ' + name + ',' \
                '\n\nThanks for contacting us.'\
                '\nWe will get back to you soon'\
                '\n\nRegards,\nBloom Interio')

            subject = 'Thanks for contacting us.'
            message = ('Hi,\n\nThanks for contacting us. We will get back to you soon.\n\n' + \
                    'Regards,\nAdmin')

            send_mail(
                subject,
                message,
                DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=True,)

            return HttpResponse('ho gya mail')
    return asdfasdfas
    return HttpResponse(request.POST)

    return HttpResponse(request.POST)
