from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import HairCutting, HairColouring, LadiesWaxing, Eyebrows, WaxPackage, MensWaxing, Massage, NonPurchasable
from .forms import ContactForm
# home views
def home(request):
    return render(request, 'home.html')

# servives views
def services(request):
    hair_cutting = HairCutting.objects.all().order_by('name')
    hair_colouring = HairColouring.objects.all().order_by('name')
    ladies_waxing = LadiesWaxing.objects.all().order_by('name')
    eyebrows = Eyebrows.objects.all().order_by('name')
    wax_package = WaxPackage.objects.all().order_by('name')
    mens_waxing = MensWaxing.objects.all().order_by('name')
    massage = Massage.objects.all().order_by('name')
    non_p = NonPurchasable.objects.all().order_by('name')

    return render(request, 'services.html',
                 {'hair_cutting': hair_cutting,
                  'hair_colouring': hair_colouring,
                  'ladies_waxing': ladies_waxing,
                  'eyebrows': eyebrows,
                  'wax_package': wax_package,
                  'mens_waxing': mens_waxing,
                  'massage': massage, 
                  'non_p': non_p
                 })  
 

# Conctact views
def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = request.POST['name'] 
            email = request.POST['email'] 
            message = request.POST['message']
            # send an email
            # send_mail(name, message, email, ['freelance.website.manager@gmail.com'])
        return render(request, 'contact.html', {'name': name, 'contact_form': contact_form})
        messages.success(request, "Thanks for your contact + {'name'} we'll get back to you shortly")
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
    