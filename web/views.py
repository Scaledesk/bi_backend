from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *
from core.utils import *
# Create your views here.

# def TestView(request):
#     """ jut for testing purpose """
#     return render(request, 'kitchen/kitchen_by_type.html', None)

def LandingView(request):
    """ To serve laning/home page """
    context = {}
    context = AppendBasicContext(context)
    # return HttpResponse(context)
    return render(request, 'landing.html', context)

def PrivacyPolicyView(request):
    """ To serve privacy policy page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'privacy_policy.html', context)

def ContactView(request):
    """ To serve Conteact page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'contact.html', context)

def AboutView(request):
    """ to serve about us page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'about.html', context)

def FAQView(request):
    """ to serve frequently asked question page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'FAQ.html', context)

def InteriorView(request):
    """ To serve Interior view / blog  page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'interior.html', context)

# def KitchenSizeView(request):
#     context = {}
#     context = AppendBasicContext(context)
#     return render(request, 'kitchen_size.html', context)

def ProductHelpView(request):
    """ to serve product help page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'product_help.html', context)

def TermsAndConditionsView(request):
    """ to serve terms and condition page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'terms_and_conditions.html', context)


def ContactRequestView(request): #user_email, activation_key, first_name
    if request.method == 'POST':
        from django.core.mail import send_mail
        from bloom_interio.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL

        name = request.POST['name']
        contact_no = request.POST['contact_no']
        user_email = request.POST['user_email']
        location = request.POST['address']
        budget = request.POST['budget']

        subject = 'contact request'
        message = ('Name: ' + name + \
            '\nContact No: ' + contact_no + \
            '\nEmail: '+ user_email + \
            '\nLocation: '+ location + \
            '\nBudget: ' + budget)

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
            return redirect("/thank-you/?source=contact")



def ModalFormView(request): #user_email, activation_key, first_name
    if request.method == 'POST':
        from django.core.mail import send_mail
        from bloom_interio.settings import DEFAULT_FROM_EMAIL, ADMIN_EMAIL
        name = request.POST['name']
        contact_no = request.POST['contact_no']
        email = request.POST['email']
        location = request.POST['address']

        subject = 'contact request'
        message = ('Name: ' + name + \
            '\nContact No: ' + contact_no + \
            '\nEmail: '+ email + \
            '\nLocation: '+ location)

        if send_mail(subject, message, DEFAULT_FROM_EMAIL, [ADMIN_EMAIL]):
            subject = 'Bloom Interio'
            message = ('Hi ' + name + ',' \
                '\n\nThanks for contacting us.'\
                '\nWe will get back to you soon'\
                '\n\nRegards,\nBloom Interio')
            subject = 'Thanks for contacting us.'
            send_mail(
                subject,
                message,
                DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,)
            return redirect("/thank-you/?source=contact")

def ThankYouView(request):
    context = {}
    context = AppendBasicContext(context)
    source = request.GET.get('source', None)
    context['source'] = source
    return render(request, "thank_you.html", context)


def ServeLandingView(request):
    """ to serve frequently asked question page """
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'index-new.html', context)

