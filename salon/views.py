from django.shortcuts import render
from .models import HairCutting, HairColouring, LadiesWaxing, Eyebrows, WaxPackage, MensWaxing, Massage, NonPurchasable

# home views
def home(request):
    return render(request, 'home.html')

# servives views
def services(request):
    hairCutting = HairCutting.objects.all().order_by('name')
    hairColouring = HairColouring.objects.all().order_by('name')
    ladiesWaxing = LadiesWaxing.objects.all().order_by('name')
    eyebrows = Eyebrows.objects.all().order_by('name')
    waxPackage = WaxPackage.objects.all().order_by('name')
    mensWaxing = MensWaxing.objects.all().order_by('name')
    massage = Massage.objects.all().order_by('name')
    nonP = NonPurchasable.objects.all().order_by('name')

    return render(request, 'services.html',
                 {'hairCutting': hairCutting,
                  'hairColouring': hairColouring,
                  'ladiesWaxing': ladiesWaxing,
                  'eyebrows': eyebrows,
                  'waxPackage': waxPackage,
                  'mensWaxing': mensWaxing,
                  'massage': massage, 
                  'nonP': nonP
                 })   

# Conctact views
def contact(request):
    return render(request, 'contact.html')