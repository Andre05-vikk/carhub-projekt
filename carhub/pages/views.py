from django.shortcuts import render
from .models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()

    data = {
        'teams': teams,
    }

    return render(request, 'pages/home.html', data)


# contact - Aimar
# services -  Sander
# about-   Andre
# Andrei - Logout