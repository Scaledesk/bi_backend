from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from core.utils import *
# Create your views here.

def TestView(request):
    """ jut for testing purpose """
    return render(request, 'kitchen/kitchen_by_type.html', None)

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
