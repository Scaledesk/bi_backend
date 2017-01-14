from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def TestView(request):
    return render(request, 'kitchen/kitchen_by_type.html', None)

def LandingView(request):
    return render(request, 'landing.html', None)

def PrivacyPolicyView(request):
    return render(request, 'privacy_policy.html', None)

def ContactView(request):
    return render(request, 'contact.html', None)

def AboutView(request):
    return render(request, 'about.html', None)

def FAQView(request):
    return render(request, 'FAQ.html', None)

def InteriorView(request):
    return render(request, 'interior.html', None)

def KitchenSizeView(request):
    return render(request, 'kitchen_size.html', None)

def ProductHelpView(request):
    return render(request, 'product_help.html', None)

def TermsAndConditionsView(request):
    return render(request, 'terms_and_conditions.html', None)
