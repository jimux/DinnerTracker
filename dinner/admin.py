from django.contrib import admin
from .models import *

admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)
admin.site.register(Dish)
admin.site.register(Dinner)
admin.site.register(Restaurant)
admin.site.register(Eater)
admin.site.register(DishOpinion)
admin.site.register(RestaurantOpinion)

