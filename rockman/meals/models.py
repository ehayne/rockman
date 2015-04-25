'''Models for the Meals Application'''
from django.db import models

class Day(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    meals = models.ForeignKey(
        'Meal',
        db_column='meals',
        blank=True,
        null=True
    )

    date = models.DateTimeField(
        unique=True
    )

    # def clean(self):
    #     # Don't allow date to be blank
    #     if self.date is None:
    #         raise ValidationError('Date is required for a meal.')


class Meal(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    meal_type = models.ForeignKey(
        'MealType',
        db_column='meal_type',
        blank=True,
        null=True
    )
    recipes = models.ForeignKey(
        'Recipe',
        db_column='recipies',
        blank=True,
        null=True
    )

    def clean(self):
        # Don't allow task to be blank
        if self.meal_type is None:
            raise ValidationError('Meal type is required.')


class MealType(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    meal_type = models.CharField(
        max_length=100,
        help_text='A label to be used for meals (ex. breakfast).',
    )
    priority = models.IntegerField(
        unique=True,
        help_text='Order that the meal types fall in a day.'
    )
    description = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        help_text='A description of the meal type.',
    )

    def clean(self):
        # Don't allow meal type to be blank. It makes no sense.
        if self.meal_type is None:
            raise ValidationError('Meal type is required.')


class Recipe(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=200,
        help_text='A description of what needs to be done.',
    )
    ingredients = models.CharField(  # TODO: this should be a key to an ingredients list - ideally it should point ot kyle's app
        max_length=2000,
        help_text='A list of ingredients for the recipe.',
        blank=True,
        null=True,
    )
    directions = models.CharField(
        max_length=2000,
        help_text='Directions for preparing the recipe.',
        blank=True,
        null=True,
    )
    notes = models.CharField(
        max_length=2000,
        help_text='Interesting notes about the recipe.',
        blank=True,
        null=True,
    )

    def clean(self):
        # Don't allow name to be blank
        if self.name is None:
            raise ValidationError('Name is required.')