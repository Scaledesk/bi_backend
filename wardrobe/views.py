from django.shortcuts import render, redirect
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
            temp['wi_sub'] = WISub.objects.filter(w_includes = obj)
            w_includes.append(temp)

        max_price = (wardrobe.base_price + (wardrobe.base_price*wardrobe.max_change)/100)
        min_price = (wardrobe.base_price + (wardrobe.base_price*wardrobe.min_change)/100)

        context['wardrobe'] = wardrobe
        context['w_images'] = w_images
        context['w_material'] = w_material
        context['w_finishing'] = w_finishing
        context['w_includes'] = w_includes
        context['w_appliances'] = w_appliances
        context['min_price'] = min_price
        context['max_price'] = max_price
        return context

def ReloadFlex(request):
    """ajax request to reload the images of wardrobe pdp """
    context={}
    color = request.POST['color']
    wardrobe_id = request.POST['wardrobe_id']
    if color =='all':
        flex_images = WImage.objects.filter(wardrobe = Wardrobe.objects.get(id=wardrobe_id))
    else:
        flex_images = WImage.objects.filter(wardrobe = Wardrobe.objects.get(id=wardrobe_id), w_color = WColor.objects.get(name=color))
    context['w_images'] = flex_images
    from django.template.loader import render_to_string
    html = render_to_string('wardrobe/reload_flex.html', context)
    return HttpResponse(html)

def ServeProduct(request, w_type_slug, theme_slug, wardrobe_slug):
    """ to serve final product based on type, theme and wardrobe """
    context = ProductContextCreator(w_type_slug, theme_slug, wardrobe_slug)
    context = AppendBasicContext(context)
    return render(request, 'wardrobe/wardrobe_pdp.html', context=context)

# def WardrobeResponse(request):
#     """ to save the response received on wardrobe product """
#     return HttpResponse(request.POST)

def ProductConsultation(request):
    if request.method == 'POST':
        from django.core.mail import send_mail
        from bloom_interio.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL

        name = request.POST['name']
        contact_no = request.POST['contact_no']
        user_email = request.POST['user_email']
        address = request.POST['address']
        color = str(request.POST['color'])
        if color == 'all':
            color = 'None'
        finish = request.POST['finish']
        material = request.POST['material']

        wardrobe_id = request.POST['wardrobe']
        wardrobe = Wardrobe.objects.get(id=wardrobe_id)
        dimension = str(wardrobe.l) +'*'+ str(wardrobe.b) +'*'+ str(wardrobe.h)

        wardrobe_theme = wardrobe.theme.name
        wardrobe_type = wardrobe.theme.w_type.name

        subject = 'Custom quote request'
        message = ('Name: ' + name + \
            '\nContact No: ' + contact_no + \
            '\nEmail: '+ user_email + \
            '\nAddress: '+ address + \
            '\nWardrobe Type: '+ wardrobe_type + \
            '\nWardrobe Theme: '+ wardrobe_theme + \
            '\nWardrobe: '+ wardrobe.name + \
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
            return redirect("/thank-you/?source=wardrobe")
