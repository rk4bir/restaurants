from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Food, FoodCategory
from restaurants.models import Restaurant

def list_view(request):
	template_name = 'foods/foods_list.html'
	food_list     = Food.objects.all()
	contex = {
		'food_list': food_list
	}
	return render(request, template_name, contex)

def detail_view(request, slug):
	food = get_object_or_404(Food, slug=slug)
	template_name = 'foods/detail.html'
	restaurants   = Restaurant.objects.all().filter(food_items=food)
	contex        = {
		'food': food,
		'restaurants': restaurants
	}
	return render(request, template_name, contex)