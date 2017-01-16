from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from core.utils import *
# Create your views here.

def TestView(request):
    return render(request, 'kitchen/kitchen_by_type.html', None)

def LandingView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'landing.html', context)

def PrivacyPolicyView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'privacy_policy.html', context)

def ContactView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'contact.html', context)

def AboutView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'about.html', context)

def FAQView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'FAQ.html', context)

def InteriorView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'interior.html', context)

def KitchenSizeView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'kitchen_size.html', context)

def ProductHelpView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'product_help.html', context)

def TermsAndConditionsView(request):
    context = {}
    context = AppendBasicContext(context)
    return render(request, 'terms_and_conditions.html', context)
