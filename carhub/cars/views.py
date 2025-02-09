from django.shortcuts import render

# Create your views here.

def cars(request):
    # Aimar
    # create cars variable and assign the Car.objects by ordering it by the created_date
    # create a car_title_search variable, then assign the distinct value list from the car objects
    # create a state_search variable, then assign the distinct value list from the car objects
    # create a year_search variable, then assign the distinct value list from the car objects
    # create a body_style_search variable, then assign the distinct value list from the car objects

    # create a data dictionary and pass down the variables above as key value pairs

    # return the render function, passing request, the cars.html template and the data
    pass

def car_detail(request, id):
    #Andre
    # Create a single_car variable that receives car object from a function called get_object_or_404
    # create a data dictionary and pass down the variable above as key value pairs
    # return the render function, passing request, the car_detail.html template and the data
    pass

def search(request):
    # Sander
    # create cars variable and assign the Car.objects by ordering it by the created_date
    # create a car_title_search variable, then assign the distinct value list from the car objects
    # create a state_search variable, then assign the distinct value list from the car objects
    # create a year_search variable, then assign the distinct value list from the car objects
    # create a body_style_search variable, then assign the distinct value list from the car objects

    #Andrei
    # Use the flow control (e.g if) to check for the keyword used in request
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    # Do the flow using if statement to allow user to search base on car_title
    # Do the flow using if statement to allow user to search base on model
    # Do the flow using if statement to allow user to search base on state
    # Do the flow using if statement to allow user to search base on year
    # Do the flow using if statement to allow user to search base on body_style
    # Do the flow using if statement to allow user to search base on min_price

    # create a data dictionary and pass down the variables above as key value pairs

    # return the render function, passing request, the car search.html template and the data
    pass
