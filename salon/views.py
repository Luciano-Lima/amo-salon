from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import HairCutting, HairColouring, LadiesWaxing, Eyebrows, WaxPackage, MensWaxing, Massage, NonPurchasable, TeamWorkOne, TeamWorkTwo, TeamWorkThree 
from .forms import ContactForm

# home views
def home(request):
    team_one = TeamWorkOne.objects.all()
    team_two = TeamWorkTwo.objects.all()
    team_three = TeamWorkThree.objects.all()
    return render (request, 'home.html', {'team_one': team_one, 'team_two': team_two, 'team_three': team_three})
    

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
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name') 
            email = form.cleaned_data.get('email') 
            message = form.cleaned_data.get('message')
            # send an email
            send_mail(name, message, email, ['freelance.website.manager@gmail.com'])
            messages.success(request, f"Thanks for your contact {name} we'll get back to you shortly!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    