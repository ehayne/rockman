from django.contrib import admin
from rockman.meals.models import Day, Meal, MealType, Recipe

class DayAdmin(admin.ModelAdmin):
    fields = (
        'meals',
        'date',
        )

    list_display = (
        'get_related_meals',
        'date',
        )
    save_on_top = True

    def get_related_meals(self, obj):
        return ', '.join(meal.__unicode__()
                         for meal in obj.meals.all())
    get_related_meals.short_description = 'Meals for the day'

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