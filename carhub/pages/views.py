from django.shortcuts import render
from .models import Team, Contact


# Create your views here.
def home(request):
    teams = Team.objects.all()

    data = {
        'teams': teams,
    }

    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    
    return render(request, 'pages/services.html')


def contact(request):
    contacts = Contact.objects.all()
    data = {
        'contacts': contacts,
    }
    return render(request, 'pages/contact.html', data)

# contact - Aimar
# services -  Sander
# about-   Andre
# Andrei - Logout