from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
# Register function
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=user_name).exixts():
                messages.error(request, 'User already exists!')
                return redirect('register')



# login - Aimar
# dashboard -  Sander
# Andre - Register
# Andrei - Logout