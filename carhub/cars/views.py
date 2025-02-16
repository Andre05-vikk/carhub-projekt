from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator

# Create your views here.

def cars(request):
    # Get all cars ordered from oldest to newest
    cars = Car.objects.order_by('-created_date')

    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # Fetch distinct values for search filters
    car_title_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # Prepare data to pass to the template
    data = {
        'cars': paged_cars,
        'car_title_search': car_title_search,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }

    # Render the cars.html template with the context data
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    # Get the car object or return 404 if not found
    single_car = get_object_or_404(Car, pk=id)
    
    # Create data dictionary with the car object
    data = {
        'single_car': single_car,
    }
    
    # Render the template with the data
    return render(request, 'cars/car_detail.html', data)

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


#  Andre - should handle the car_detail html