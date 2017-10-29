from __future__ import unicode_literals

from django.db import models


FOOD_GROUPS = (
    ('meat', 'meat'),
    ('grain', 'grain'),
    ('vegetable', 'vegetable'),
    ('fruit', 'fruit'),
    ('dairy', 'dairy')
)


APPROVALS = (
    ('like', 'like'),
    ('dislike', 'dislike'),
    ('meh', 'meh')
)


UNITS = (
  ('count','count'),
  ('oz','oz'),
  ('tablespoon', 'tablespoon'),
  ('teaspoon', 'teaspoon'),
  ('cups', 'cups'),
  ('clove', 'clove'),
  ('grams', 'grams'),
  ('thumb', 'thumb'),
)


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey('Ingredient', related_name='ingredient')
    dishes = models.ForeignKey('Dish', related_name='ingredients')
    quantity = models.DecimalField(max_digits=6, decimal_places=3)
    unit = models.CharField(choices=UNITS, max_length=100)


class Dish(models.Model):
    name = models.CharField(max_length=200)
    primary_food_group = models.CharField(choices=FOOD_GROUPS, max_length=20)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Dinner(models.Model):
    name = models.CharField(max_length=400)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Eater(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class DishOpinion(models.Model):
    approval = models.CharField(choices=APPROVALS, max_length=20)
    eater = models.ForeignKey('Eater', related_name='dishopinions')
    dish = models.ForeignKey('Dish', related_name='opinions')


class RestaurantOpinion(models.Model):
    approval = models.CharField(choices=APPROVALS, max_length=20)
    eater = models.ForeignKey('Eater', related_name='restaurantopinions')
    restaurant = models.ForeignKey('Restaurant', related_name='opinions')
