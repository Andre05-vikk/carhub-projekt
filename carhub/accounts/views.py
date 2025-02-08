from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Register function
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Checking if username already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        # Checking if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use!')
            return redirect('register')

        # Checking if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        # Creating the user
        user = User.objects.create_user(username=user_name, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')



# login - Aimar
# dashboard -  Sander
# Andre - Register
# Andrei - Logout