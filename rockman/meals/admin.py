from django.contrib import admin
from rockman.meals.models import Day, Meal, MealType, Recipe

class DayAdmin(admin.ModelAdmin):
    pass

admin.site.register(Day, DayAdmin)


class MealAdmin(admin.ModelAdmin):
    pass

admin.site.register(Meal, MealAdmin)


class MealTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(MealType, MealTypeAdmin)


class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)