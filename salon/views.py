from django.shortcuts import render

# home views
def home(request):
    return render(request, 'home.html')

# servives views
def services(request):
    return render(request, 'services.html')   

# Conctact views
def contact(request):
    return render(request, 'contact.html')