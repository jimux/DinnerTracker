from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    ingredients = Ingredient.objects.all()
    dishes = Dish.objects.all()
    dinners = Dinner.objects.all()
    restaurants = Restaurant.objects.all()
    eaters = Eater.objects.all()
    dishOpinions = DishOpinion.objects.all()
    restaurantOpinions = RestaurantOpinion.objects.all()
    template = loader.get_template('dinner/index.html')
    context = {
        'ingredients': ingredients,
        'dishes': dishes,
        'dinners': dinners,
        'restaurants': restaurants,
        'eaters': eaters,
        'dishOpinions': dishOpinions,
        'restaurantOpinions': restaurantOpinions,
    }
    return HttpResponse(template.render(context, request))
