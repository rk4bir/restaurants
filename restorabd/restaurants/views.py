from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Restaurant, ServiceTime, RestaurantReview
from reviews.models import Review
from general.functions import getReviewStatus
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from notifications.models import Notification


def restauranJson_view(request):
    '''restaurants = Restaurant.objects.all().filter(is_active=True)
    data        = serializers.serialize('json', restaurants)
    return HttpResponse(data, content_type='application/json')'''
    #return JsonResponse(restaurants)
    r = Notification.objects.first()
    return render(request, 'test.html', {'r': r})

def restaurant_list(request):
    template_name = 'restaurants/restaurants_list.html'
    if request.is_ajax() and request.method == "POST":
        request_data = int(request.POST['dataNo'])
        restaurants = Restaurant.objects.all().filter(is_active=True)[request_data:(request_data+10)]
        return render(request, 'restaurants/load_more_restaurant.html', {'restaurants': restaurants})
    restaurants   = Restaurant.objects.all().filter(is_active=True)[:20]
    contex        = {
        'restaurants': restaurants
    }

    return render(request, template_name, contex)

def restaurant_detail(request, slug):
    try:
        restaurant = Restaurant.objects.get(slug=slug)
    except:
        return HttpResponseRedirect("/404notfound/")
    service_times = ServiceTime.objects.get(restaurant=restaurant)
    review        = RestaurantReview.objects.all().filter(restaurant=restaurant)
    template_name = 'restaurants/detail.html'
    contex        = {
        'restaurant': restaurant,
        'service_times': service_times,
        'active_d': 'tab_a_active',
        'foods': restaurant.food_items.all(),
        'review': review,
    }

    return render(request, template_name, contex)



def restaurant_review(request, slug):
    restaurant    = get_object_or_404(Restaurant, slug=slug)
    template_name = 'restaurants/review.html'
    review        = RestaurantReview.objects.get(restaurant=restaurant)
    service_times = ServiceTime.objects.get(restaurant=restaurant)
    food          = getReviewStatus(review.food)
    price         = getReviewStatus(review.price)
    service       = getReviewStatus(review.service)
    environment   = getReviewStatus(review.environment)
    user_reviews  = Review.objects.all().filter(restaurant=restaurant)
    contex        = {
        'review': review,
        'restaurant': restaurant,
        'active_r': 'tab_a_active',
        'service_times': service_times,
        'user_reviews': user_reviews,
        'food': food,
        'service': service,
        'price': price,
        'environment': environment
    }

    return render(request, template_name, contex)

