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
    cars = Car.objects.order_by('-created_date')  # Fetch all cars initially

    car_title = request.GET.get('car_title')
    model = request.GET.get('model')
    state = request.GET.get('state')
    year = request.GET.get('year')
    body_style = request.GET.get('body_style')
    transmission = request.GET.get('transmission')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if car_title and car_title.strip():
        cars = cars.filter(car_title__iexact=car_title.strip())

    if model and model.strip():
        cars = cars.filter(model__iexact=model.strip())

    if state and state.strip():
        cars = cars.filter(state__iexact=state.strip())

    if year and year.strip():
        cars = cars.filter(year__iexact=year.strip())

    if body_style and body_style.strip():
        cars = cars.filter(body_style__iexact=body_style.strip())

    if transmission and transmission.strip():
        cars = cars.filter(transmission__iexact=transmission.strip())

    if min_price and max_price:
        try:
            min_price = int(min_price)
            max_price = int(max_price)
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass  # Ignore invalid input

    # Fetch distinct values for dropdown menus
    car_title_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    data = {
        'cars': cars,
        'car_title_search': car_title_search,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
        'cars': cars if request.GET else None,
    }

    return render(request, 'cars/search.html', data)

#  Andre - should handle the car_detail html